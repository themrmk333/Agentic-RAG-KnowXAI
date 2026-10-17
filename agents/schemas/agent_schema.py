"""Structured output and Pydantic schemas for Agentic RAG agents."""

from typing import List, Optional
from pydantic import BaseModel, Field


class UnderstoodQuery(BaseModel):
    """Schema for Query Understanding output."""

    rephrased_query: str = Field(
        description="The rephrased, search-optimized version of the user query."
    )
    intent: str = Field(
        description=(
            "Determined intent category: coding, mathematics, research, "
            "it, hr, finance, project, management, sales, greeting, or general."
        )
    )
    key_terms: List[str] = Field(
        default_factory=list,
        description="Key search terms extracted from the query for RAG retrieval."
    )


class AgentPlan(BaseModel):
    """Schema for Planner output."""

    specialists: List[str] = Field(
        description=(
            "Allowed specialists: research, coding, mathematics, critic, "
            "decision, it, hr, finance, project. For management queries, "
            "use decision and, when useful, research and critic."
        )
    )
    justification: str = Field(
        description="Reasoning explaining why these specific specialists are required or not."
    )


class FinalAnswer(BaseModel):
    """Schema for final synthesized answer from the Aggregator."""

    answer: str = Field(
        description="The final synthesized answer, formatted using rich Markdown."
    )
    confidence: float = Field(
        description="Confidence score between 0.0 and 1.0 based on specialist agreement and context alignment."
    )
    references: List[str] = Field(
        default_factory=list,
        description="List of sources, links, or documents referenced in compiling an answer."
    )
    errors_encountered: List[str] = Field(
        default_factory=list,
        description="Any non-blocking errors encountered during the pipeline."
    )