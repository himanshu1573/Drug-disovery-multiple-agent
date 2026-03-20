from __future__ import annotations

from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from agents.schema import (
    CollectorRequest,
    PlanDecisionInput,
    ReviewDecisionInput,
    SourceName,
)


class CreateRunInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    gene_symbol: str = Field(..., min_length=1)
    disease_id: str | None = None
    objective: str | None = None
    sources: list[SourceName] | None = None
    per_source_top_k: int = Field(default=10, ge=1, le=20)
    max_literature_articles: int = Field(default=5, ge=1, le=20)
    model_override: str | None = None
    run_id: str | None = None

    def to_request(self) -> CollectorRequest:
        return CollectorRequest(
            gene_symbol=self.gene_symbol,
            disease_id=self.disease_id,
            objective=self.objective,
            sources=self.sources
            or [
                SourceName.DEPMAP,
                SourceName.PHAROS,
                SourceName.OPENTARGETS,
                SourceName.LITERATURE,
            ],
            per_source_top_k=self.per_source_top_k,
            max_literature_articles=self.max_literature_articles,
            model_override=self.model_override,
            run_id=self.run_id or f"run-{uuid4().hex[:12]}",
        )


class CreateRunResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    run_id: str
    status: str = "started"


class ResumeRunResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    run_id: str
    status: str = "resumed"


class PlanDecisionBody(PlanDecisionInput):
    pass


class ReviewDecisionBody(ReviewDecisionInput):
    pass


class CreateRunFromTextInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    message: str = Field(..., min_length=1)
    sources: list[SourceName] | None = None
    per_source_top_k: int = Field(default=10, ge=1, le=20)
    max_literature_articles: int = Field(default=5, ge=1, le=20)
    model_override: str | None = None
    run_id: str | None = None


class FollowupInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    message: str = Field(..., min_length=1)
    urls: list[str] | None = None


class FollowupResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    run_id: str
    answer_markdown: str
    target_switch_detected: bool = False
    extracted_gene_symbol: str | None = None
    used_urls: list[str] = Field(default_factory=list)
