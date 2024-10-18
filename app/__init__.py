from fastapi import APIRouter
from app.auth.auth_backend import image_router as auth_image_router
from app.question.api import router as question_router
from app.question.api import router_type as question_type_router

router = APIRouter()

router.include_router(auth_image_router, prefix="/auth/image", tags=["auth"])
router.include_router(question_router, prefix="/question", tags=["Question"])
router.include_router(question_type_router, prefix="/question/type", tags=["Question Type"])


