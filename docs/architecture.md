# Architecture Overview

## System Design

Cidadania AI follows a clean client-server architecture with a stateless REST API backend
and a single-page application frontend.

## Request Flow

```
User → React SPA → FastAPI Backend → OpenAI API
                        ↓
                 Rights Knowledge Base (RAG context)
                        ↓
                 Language Detection Service
                        ↓
                 PDF Generator (fpdf2)
```

## Key Design Decisions

**Stateless backend:** The API does not store user sessions. Each request is self-contained,
which simplifies scaling and reduces privacy risk.

**RAG over fine-tuning:** Instead of fine-tuning a model on legal texts (expensive and slow
to update), we inject relevant legal context at inference time. This allows the knowledge
base to be updated without retraining.

**Language detection:** The service automatically detects whether the user is writing in
Portuguese or English and responds accordingly, making the tool accessible to both
Brazilian and Irish communities.

**PDF generation server-side:** Documents are generated on the backend to ensure consistent
formatting regardless of the user's browser or OS.

## Component Map

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | React + TypeScript + TailwindCSS | User interface, form submission |
| Backend API | Python + FastAPI | Request handling, AI orchestration |
| AI Service | OpenAI GPT-4o-mini | Natural language understanding and generation |
| Rights KB | Static Python dict (RAG) | Legal context injection |
| Language Service | Keyword-based detection | PT/EN routing |
| Document Service | fpdf2 | PDF generation for official documents |
| Containerisation | Docker + docker-compose | Local and cloud deployment |
