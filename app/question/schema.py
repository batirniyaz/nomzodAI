import datetime

from pydantic import BaseModel, Field
from typing import Optional


class QuestionBase(BaseModel):
    text: str = Field(..., description="The question")
    answer: str = Field(..., description="The answer")
    type_id: int = Field(..., description="The ID of the question type")


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    text: Optional[str] = Field(None, description="The question")
    answer: Optional[str] = Field(None, description="The answer")
    type_id: Optional[int] = Field(None, description="The ID of the question type")


class QuestionResponse(QuestionBase):
    id: int = Field(..., description="The ID of the question")
    type: "QuestionTypeResponse" = Field(None, description="The type of the question")

    created_at: datetime.datetime = Field(..., description="The time the question was created")
    updated_at: datetime.datetime = Field(..., description="The time the question was updated")

    class Config:
        from_attributes = True
        validate_assignment = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "text": "What is the capital of Uzbekistan?",
                "answer": "Tashkent",
                "type_id": 1,
                "type": "Multiple Choice",
                "created_at": "2021-08-01T12:00:00",
                "updated_at": "2021-08-01T12:00:00"
            }
        }
        arbitrary_types_allowed = True


class QuestionTypeBase(BaseModel):
    typeName: str = Field(..., description="The type of the question")


class QuestionTypeCreate(QuestionTypeBase):
    pass


class QuestionTypeUpdate(QuestionTypeBase):
    typeName: Optional[str] = Field(None, description="The type of the question")


class QuestionTypeResponse(QuestionTypeBase):
    id: int = Field(..., description="The ID of the question type")
    questions: list[QuestionResponse] = Field([], description="A list of questions associated with the type")

    created_at: datetime.datetime = Field(..., description="The time the question type was created")
    updated_at: datetime.datetime = Field(..., description="The time the question type was updated")

    class Config:
        from_attributes = True
        validate_assignment = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "typeName": "Multiple Choice",
                "questions": [
                    {
                        "id": 1,
                        "text": "What is the capital of Uzbekistan?",
                        "answer": "Tashkent",
                        "type_id": 1,
                        "created_at": "2021-08-01T12:00:00",
                        "updated_at": "2021-08-01T12:00:00"
                    }
                ],
                "created_at": "2021-08-01T12:00:00",
                "updated_at": "2021-08-01T12:00:00"
            }
        }
        arbitrary_types_allowed = True
