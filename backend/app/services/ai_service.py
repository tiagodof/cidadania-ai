import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT_PT = """Você é um assistente especializado em direitos dos cidadãos brasileiros e irlandeses.
Seu papel é explicar direitos de forma clara, acessível e precisa, sempre citando a legislação relevante.
Você NÃO fornece aconselhamento jurídico. Sempre oriente o usuário a consultar um advogado para casos específicos.
Responda sempre em português do Brasil, de forma objetiva e empática."""

SYSTEM_PROMPT_EN = """You are an assistant specialised in Brazilian and Irish citizens' rights.
Your role is to explain rights clearly, accessibly and accurately, always citing relevant legislation.
You do NOT provide legal advice. Always advise the user to consult a solicitor for specific cases.
Respond in English, in an objective and empathetic manner."""

DISCLAIMER_PT = "Esta resposta é apenas informativa e não constitui aconselhamento jurídico. Consulte um advogado para orientação específica ao seu caso."
DISCLAIMER_EN = "This response is for informational purposes only and does not constitute legal advice. Please consult a qualified solicitor for guidance specific to your situation."


async def get_rights_advice(question: str, category: str, language: str) -> dict:
    system_prompt = SYSTEM_PROMPT_PT if language == "pt" else SYSTEM_PROMPT_EN
    disclaimer = DISCLAIMER_PT if language == "pt" else DISCLAIMER_EN

    category_context = {
        "consumer": "Foco em direitos do consumidor (CDC - Lei 8.078/90, Consumer Rights Act 2022).",
        "labour":   "Foco em direitos trabalhistas (CLT, Employment Equality Acts).",
        "housing":  "Foco em direito à moradia (Estatuto da Cidade, Residential Tenancies Act).",
        "civil":    "Foco em direitos civis e constitucionais (CF/88, Irish Constitution).",
        "general":  "",
    }

    context_hint = category_context.get(category, "")
    user_message = f"{context_hint}\n\nPergunta: {question}" if context_hint else question

    response = await client.chat.completions.create(
        model=os.getenv("AI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.3,
        max_tokens=800,
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "category": category,
        "sources": [],
        "disclaimer": disclaimer,
    }
