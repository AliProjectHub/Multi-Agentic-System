# grade_question.py
from pydantic import BaseModel, Field

class GradeQuestion(BaseModel):
    """Classify a question into specific topics related to Sonnen-Apotheke or other themes."""

    score: str = Field(
        description="Classify the question into one of these categories: 'Sonnen-Apotheke_Info', 'Medical_Question', 'General_Knowledge', 'Unrelated'."
    )
