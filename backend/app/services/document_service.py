import os
from openai import AsyncOpenAI
from fpdf import FPDF
from datetime import date

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DOCUMENT_PROMPTS = {
    "complaint": {
        "pt": "Redija uma carta de reclamação formal e profissional com base no seguinte contexto: {context}. Use linguagem formal, cite os direitos violados e solicite uma resolução específica.",
        "en": "Draft a formal complaint letter based on the following context: {context}. Use formal language, cite the rights violated and request a specific resolution.",
    },
    "appeal": {
        "pt": "Redija um recurso administrativo formal com base no seguinte contexto: {context}. Apresente os argumentos de forma clara e estruturada.",
        "en": "Draft a formal administrative appeal based on the following context: {context}. Present the arguments clearly and in a structured manner.",
    },
    "request": {
        "pt": "Redija um requerimento formal dirigido ao órgão público competente com base no seguinte contexto: {context}.",
        "en": "Draft a formal public service request addressed to the relevant authority based on the following context: {context}.",
    },
}


async def generate_document(doc_type: str, context: dict, language: str) -> bytes:
    prompt_template = DOCUMENT_PROMPTS[doc_type][language]
    prompt = prompt_template.format(context=str(context))

    response = await client.chat.completions.create(
        model=os.getenv("AI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1000,
    )

    document_text = response.choices[0].message.content

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.set_margins(20, 20, 20)

    pdf.set_font("Helvetica", "B", 14)
    title = {"complaint": "Carta de Reclamação", "appeal": "Recurso", "request": "Requerimento"}
    pdf.cell(0, 10, title.get(doc_type, "Documento"), ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Helvetica", size=10)
    pdf.cell(0, 8, f"Data: {date.today().strftime('%d/%m/%Y')}", ln=True, align="R")
    pdf.ln(5)

    pdf.set_font("Helvetica", size=11)
    for line in document_text.split("\n"):
        pdf.multi_cell(0, 7, line)

    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 9)
    disclaimer = "Documento gerado com auxílio de Inteligência Artificial. Não constitui aconselhamento jurídico."
    pdf.multi_cell(0, 6, disclaimer)

    return bytes(pdf.output())
