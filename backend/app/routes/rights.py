from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import get_rights_advice

router = APIRouter()


class RightsQuery(BaseModel):
    question: str
    category: str = "general"  # consumer, labour, housing, civil, general
    language: str = "pt"       # pt or en


class RightsResponse(BaseModel):
    answer: str
    category: str
    sources: list[str]
    disclaimer: str


@router.post("/ask", response_model=RightsResponse)
async def ask_rights_question(query: RightsQuery):
    """
    Ask a question about civic rights and receive an AI-powered answer
    grounded in relevant legislation.
    """
    if not query.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    result = await get_rights_advice(
        question=query.question,
        category=query.category,
        language=query.language,
    )
    return result


@router.get("/categories")
def list_categories():
    """Return available rights categories."""
    return {
        "categories": [
            {"id": "consumer", "label_pt": "Direitos do Consumidor", "label_en": "Consumer Rights"},
            {"id": "labour",   "label_pt": "Direitos Trabalhistas",  "label_en": "Labour Rights"},
            {"id": "housing",  "label_pt": "Direito à Moradia",      "label_en": "Housing Rights"},
            {"id": "civil",    "label_pt": "Direitos Civis",         "label_en": "Civil Rights"},
            {"id": "general",  "label_pt": "Geral",                  "label_en": "General"},
        ]
    }
