from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from datetime import datetime

from app.database import get_db
from app.models.url import URL
from app.schemas.url_schema import URLCreate
from app.utils.shortener import generate_short_code
from app.utils.auth_bearer import get_current_user
from app.models.user import User
router = APIRouter(prefix="/url", tags=["URL"])


@router.post("/shorten")
def shorten_url(
    data: URLCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    short_code = generate_short_code()

    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = URL(
        original_url=str(data.url),
        short_code=short_code,
        clicks=0,
        user_id=current_user.id
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "short_url": f"http://localhost:8000/url/{short_code}"
    }

# GET ALL URLS
@router.get("/all")
def get_urls(db: Session = Depends(get_db)):
    return db.query(URL).all()

# DELETE URL
@router.delete("/{url_id}")
def delete_url(
    url_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    url = db.query(URL).filter(
        URL.id == url_id,
        URL.user_id == current_user.id
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    db.delete(url)
    db.commit()

    return {
        "message": "Deleted successfully"
    }

# REDIRECT URL
@router.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    url.clicks += 1
    url.last_accessed = datetime.utcnow()

    db.commit()

    return RedirectResponse(url.original_url)