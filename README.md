# 🏛️ Cidadania AI

> **AI-powered civic rights assistant** — helping citizens understand their rights, navigate public services, and draft official documents using Artificial Intelligence.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5+-3178C6.svg)](https://typescriptlang.org)

---

## 🎯 What is Cidadania AI?

Cidadania AI is a free, open-source web application that uses Artificial Intelligence to empower citizens with knowledge about their legal rights and help them interact with public services more effectively.

Inspired by tools like [FirstStep](https://firststep-nine.vercel.app), which democratises business planning through AI, Cidadania AI applies the same philosophy to civic life — giving ordinary people the structured knowledge and document templates they need to navigate bureaucracy with confidence.

> **This tool does not replace a lawyer.** It helps you understand your situation, prepare the right questions, and walk into a legal consultation already informed.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Rights Advisor** | Ask questions about your consumer, labour, housing, or civil rights in plain language |
| **Document Generator** | Generate formal complaint letters, appeals, and public service requests |
| **Service Finder** | Locate the correct public agency for your specific issue |
| **Step-by-Step Guides** | Structured workflows for common civic processes (e.g., filing a Procon complaint) |
| **Multilingual** | Available in Portuguese 🇧🇷 and English 🇮🇪 |

---

## 🏗️ Architecture

```
cidadania-ai/
├── frontend/               # React + TypeScript + TailwindCSS
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── utils/
├── backend/                # Python FastAPI
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   │   ├── ai_service.py       # LLM integration (RAG)
│   │   │   ├── document_service.py # PDF generation
│   │   │   └── rights_service.py   # Rights knowledge base
│   │   └── models/
├── docs/
└── docker-compose.yml
```

---

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- Python 3.11+
- OpenAI or Gemini API key

### Installation

```bash
git clone https://github.com/tiagodof/cidadania-ai.git
cd cidadania-ai

# Backend
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add your OPENAI_API_KEY to .env
uvicorn app.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

---

## 🤖 AI Integration

Cidadania AI uses a **Retrieval-Augmented Generation (RAG)** architecture:

1. A curated knowledge base of Brazilian and Irish civic rights legislation is indexed.
2. User queries are matched against relevant legal context.
3. The LLM generates a response grounded in retrieved context, minimising hallucination.

---

## 🌍 Social Impact

Access to legal information is a fundamental right, yet it remains inaccessible to millions due to complexity, language barriers, and cost. Cidadania AI aims to bridge this gap by:

- Reducing dependence on expensive legal consultations for simple matters
- Empowering immigrants and minorities to understand their rights in a new country
- Helping citizens hold institutions accountable through properly drafted formal complaints

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## ⚠️ Disclaimer

Cidadania AI provides general civic information only. It does not constitute legal advice. Always consult a qualified legal professional for matters with significant legal consequences.
