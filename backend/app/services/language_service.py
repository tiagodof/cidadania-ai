"""
Language detection service.
Detects whether the user is writing in Portuguese or English
so the AI can respond in the same language.
"""

PT_KEYWORDS = {
    "meu", "minha", "tenho", "quero", "preciso", "como", "qual", "quando",
    "direito", "empresa", "trabalho", "aluguel", "multa", "procon", "lei",
    "contrato", "salário", "demissão", "reclamação", "consumidor",
}

EN_KEYWORDS = {
    "my", "have", "want", "need", "how", "what", "when", "right", "company",
    "work", "rent", "fine", "law", "contract", "salary", "dismissal",
    "complaint", "consumer", "tenant", "employer",
}


def detect_language(text: str) -> str:
    """
    Returns 'pt' or 'en' based on keyword frequency.
    Defaults to 'pt' if ambiguous.
    """
    words = set(text.lower().split())
    pt_score = len(words & PT_KEYWORDS)
    en_score = len(words & EN_KEYWORDS)
    return "en" if en_score > pt_score else "pt"


def get_system_prompt(language: str, category: str, context_items: list[str]) -> str:
    """Builds the system prompt for the AI based on language and category."""
    context_block = "\n".join(f"- {item}" for item in context_items) if context_items else ""

    if language == "en":
        return f"""You are a civic rights assistant helping people understand their legal rights.
Category: {category}

Relevant legal references:
{context_block}

Rules:
- Always respond in English.
- Be clear, empathetic, and accessible — avoid legal jargon.
- Cite the specific law or article when relevant.
- If unsure, recommend consulting a qualified lawyer.
- Never give advice that could harm the user."""
    else:
        return f"""Você é um assistente de direitos do cidadão que ajuda pessoas a entenderem seus direitos legais.
Categoria: {category}

Referências legais relevantes:
{context_block}

Regras:
- Responda sempre em Português.
- Seja claro, empático e acessível — evite jargão jurídico.
- Cite a lei ou artigo específico quando relevante.
- Se não tiver certeza, recomende consultar um advogado qualificado.
- Nunca dê conselhos que possam prejudicar o usuário."""
