import datetime

from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.auth.database import Base


class QuestionType(Base):
    __tablename__ = 'question_type'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    typeName: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="type", lazy="selectin")

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                          default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                          default=lambda: datetime.datetime.now(datetime.timezone.utc),
                                                          onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))


class Question(Base):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    answer: Mapped[str] = mapped_column(String(255), nullable=False)

    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("question_type.id"), nullable=False)
    type: Mapped["QuestionType"] = relationship("QuestionType", back_populates="questions", lazy="selectin")

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                          default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                          default=lambda: datetime.datetime.now(datetime.timezone.utc),
                                                          onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
