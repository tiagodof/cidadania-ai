"""
Knowledge base service for civic rights.
Provides structured context to the AI for RAG-based responses.
"""

RIGHTS_CONTEXT = {
    "consumer": [
        "CDC Art. 6: direito à informação adequada e clara sobre produtos e serviços.",
        "CDC Art. 18: vícios do produto — prazo de 30 dias para reclamação (não duráveis) e 90 dias (duráveis).",
        "CDC Art. 42: proibição de cobrança vexatória de dívidas.",
        "Consumer Rights Act 2022 (Ireland): right to repair, replace, or refund within 2 years.",
    ],
    "labour": [
        "CLT Art. 7: salário mínimo, 13º salário, férias remuneradas, FGTS.",
        "CLT Art. 59: horas extras limitadas a 2h/dia, com adicional de 50%.",
        "Employment Equality Acts 1998–2015 (Ireland): protection against discrimination.",
        "Organisation of Working Time Act 1997 (Ireland): max 48h/week average.",
    ],
    "housing": [
        "Estatuto da Cidade (Lei 10.257/01): função social da propriedade urbana.",
        "Lei do Inquilinato (Lei 8.245/91): direitos e deveres de locatários.",
        "Residential Tenancies Act 2004 (Ireland): tenant rights, notice periods, rent pressure zones.",
    ],
    "civil": [
        "CF/88 Art. 5: igualdade perante a lei, liberdade de expressão, inviolabilidade do domicílio.",
        "CF/88 Art. 37: princípios da administração pública (legalidade, impessoalidade, moralidade).",
        "Irish Constitution Art. 40: personal rights, equality before the law.",
    ],
}


def get_context_for_category(category: str) -> list[str]:
    return RIGHTS_CONTEXT.get(category, [])
