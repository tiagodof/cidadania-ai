from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.services.document_service import generate_document
import io

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str   # complaint, appeal, request
    context: dict
    language: str = "pt"


@router.post("/generate")
async def create_document(request: DocumentRequest):
    """
    Generate a formal civic document (complaint, appeal, public request)
    based on user-provided context, using AI to fill in the appropriate
    legal language.
    """
    supported_types = ["complaint", "appeal", "request"]
    if request.document_type not in supported_types:
        raise HTTPException(
            status_code=400,
            detail=f"Document type must be one of: {supported_types}"
        )

    pdf_bytes = await generate_document(
        doc_type=request.document_type,
        context=request.context,
        language=request.language,
    )

    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={request.document_type}.pdf"},
    )


@router.get("/types")
def list_document_types():
    """Return available document types."""
    return {
        "types": [
            {"id": "complaint", "label_pt": "Carta de Reclamação", "label_en": "Complaint Letter"},
            {"id": "appeal",    "label_pt": "Recurso",             "label_en": "Appeal"},
            {"id": "request",   "label_pt": "Requerimento",        "label_en": "Public Request"},
        ]
    }
