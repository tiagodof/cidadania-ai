from fastapi import APIRouter

router = APIRouter()

CATEGORIES = [
    {"id": "consumer",    "label_pt": "Direitos do Consumidor", "label_en": "Consumer Rights"},
    {"id": "labour",      "label_pt": "Direitos Trabalhistas",  "label_en": "Labour Rights"},
    {"id": "housing",     "label_pt": "Direito à Moradia",      "label_en": "Housing Rights"},
    {"id": "civil",       "label_pt": "Direitos Civis",         "label_en": "Civil Rights"},
    {"id": "immigration", "label_pt": "Direito de Imigração",   "label_en": "Immigration Rights"},
    {"id": "general",     "label_pt": "Geral",                  "label_en": "General"},
]


@router.get("/categories", summary="List available rights categories")
def list_categories():
    """Returns all available rights categories with labels in PT and EN."""
    return {"categories": CATEGORIES}
