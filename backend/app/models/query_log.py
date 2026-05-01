"""
Query log model — stores anonymised user queries for improvement purposes.
No personally identifiable information is stored.
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class QueryLog:
    question_hash: str   # SHA-256 of the question (anonymised)
    category: str
    language: str
    response_tokens: int
    created_at: datetime = field(default_factory=datetime.utcnow)
