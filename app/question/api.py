from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth_backend import current_active_user
from app.auth.database import get_async_session, User

from app.question.crud import create_question, get_questions, get_question_by_id, get_questions_by_type, \
    update_question, delete_question, create_question_type, get_question_types, get_question_type_by_id, \
    update_question_type, delete_question_type
from app.question.schema import QuestionCreate, QuestionResponse, QuestionUpdate, QuestionTypeResponse, \
    QuestionTypeCreate

router = APIRouter()


@router.post("/")
async def create_question_endpoint(
        question: QuestionCreate = Query(..., description="The question details"),
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await create_question(db, question)


@router.get("/")
async def get_questions_endpoint(
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await get_questions(db)


@router.get("/{question_id}")
async def get_question_by_id_endpoint(
        question_id: int,
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await get_question_by_id(db, question_id)


@router.get("/types/{type_id}")
async def get_questions_by_type_endpoint(
        type_id: int,
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await get_questions_by_type(db, type_id)


@router.put("/{question_id}")
async def update_question_endpoint(
        question_id: int,
        question: QuestionUpdate = Query(..., description="The question details"),
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await update_question(db, question_id, question)


@router.delete("/{question_id}")
async def delete_question_endpoint(
        question_id: int,
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await delete_question(db, question_id)


router_type = APIRouter()


@router_type.post("/", response_model=QuestionTypeResponse)
async def create_question_type_endpoint(
        question_type: QuestionTypeCreate = Query(..., description="The question type details"),
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await create_question_type(db, question_type)


@router_type.get("/")
async def get_question_types_endpoint(
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    try:
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

        return await get_question_types(db)
    except Exception as e:
        raise e


@router_type.get("/{type_id}")
async def get_question_type_by_id_endpoint(
        type_id: int,
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await get_question_type_by_id(db, type_id)


@router_type.put("/{type_id}")
async def update_question_type_endpoint(
        type_id: int,
        question_type: QuestionTypeCreate = Query(..., description="The question type details"),
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await update_question_type(db, type_id, question_type)


@router_type.delete("/{type_id}")
async def delete_question_type_endpoint(
        type_id: int,
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await delete_question_type(db, type_id)

