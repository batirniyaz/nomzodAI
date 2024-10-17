from fastapi import APIRouter
from app.auth.auth_backend import image_router as auth_image_router

router = APIRouter()

router.include_router(auth_image_router, prefix="/auth/image", tags=["auth"])


