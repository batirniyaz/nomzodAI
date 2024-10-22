from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from app.question.model import Question, QuestionType
from app.question.schema import QuestionCreate, QuestionUpdate, QuestionTypeCreate


async def create_question(db: AsyncSession, question: QuestionCreate):
    try:
        question_type = get_question_type_by_id(db, question.type_id)
        if not question_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question type not found")

        question = Question(**question.model_dump())

        db.add(question)
        await db.commit()
        return question

    except Exception as e:
        await db.rollback()
        raise e


async def get_questions(db: AsyncSession):
    try:
        res = await db.execute(select(Question))
        questions = res.scalars().all()

        if not questions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Questions not found")

        return questions
    except Exception as e:
        raise e


async def get_question_by_id(db: AsyncSession, question_id: int):
    try:
        res = await db.execute(select(Question).filter_by(id=question_id))
        question = res.scalars().first()

        if not question:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

        return question
    except Exception as e:
        raise e


async def get_questions_by_type(db: AsyncSession, type_id: int):
    try:
        res = await db.execute(select(Question).filter_by(type_id=type_id))
        questions = res.scalars().all()

        if not questions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Questions not found")

        return questions
    except Exception as e:
        raise e


async def update_question(db: AsyncSession, question_id: int, question: QuestionUpdate):
    try:
        res = await db.execute(select(Question).filter_by(id=question_id))
        db_question = res.scalars().first()

        if not db_question:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

        question_type = get_question_type_by_id(db, question.type_id)
        if not question_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question type not found")

        for key, value in question.model_dump(exclude_unset=True).items():
            setattr(db_question, key, value)

        db.add(db_question)
        await db.commit()
        await db.refresh(db_question)

        return db_question
    except Exception as e:
        await db.rollback()
        raise e


async def delete_question(db: AsyncSession, question_id: int):
    try:
        res = await db.execute(select(Question).filter_by(id=question_id))
        db_question = res.scalars().first()

        if not db_question:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

        await db.delete(db_question)
        await db.commit()
        return {"status": "success", "msg": "Question deleted successfully"}
    except Exception as e:
        await db.rollback()
        raise e


async def create_question_type(db: AsyncSession, question_type: QuestionTypeCreate):
    try:
        question_type = QuestionType(**question_type.model_dump())
        db.add(question_type)
        await db.commit()
        return question_type

    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Question type already exists (must be unique)")

    except Exception as e:
        await db.rollback()
        raise e


async def get_question_types(db: AsyncSession):
    try:
        res = await db.execute(select(QuestionType))
        question_types = res.scalars().all()

        if not question_types:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question types not found")

        return question_types
    except Exception as e:
        raise e


async def get_question_type_by_id(db: AsyncSession, type_id: int):
    try:
        res = await db.execute(select(QuestionType).filter_by(id=type_id))
        question_type = res.scalars().first()

        if not question_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question type not found")

        return question_type
    except Exception as e:
        raise e


async def update_question_type(db: AsyncSession, type_id: int, question_type: QuestionTypeCreate):
    try:
        res = await db.execute(select(QuestionType).filter_by(id=type_id))
        db_question_type = res.scalars().first()

        if not db_question_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question type not found")

        for key, value in question_type.model_dump(exclude_unset=True).items():
            setattr(db_question_type, key, value)

        db.add(db_question_type)
        await db.commit()
        await db.refresh(db_question_type)

        return db_question_type
    except Exception as e:
        await db.rollback()
        raise e


async def delete_question_type(db: AsyncSession, type_id: int):
    try:
        res = await db.execute(select(QuestionType).filter_by(id=type_id))
        db_question_type = res.scalars().first()

        if not db_question_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question type not found")

        await db.delete(db_question_type)
        await db.commit()
        return {"status": "success", "msg": "Question type deleted successfully"}
    except Exception as e:
        await db.rollback()
        raise e
