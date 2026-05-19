from datetime import date

from pydantic import BaseModel


class OpportunityCreate(BaseModel):
    title: str
    agency_name: str | None = None
    date_received: date | None = None
    deadline: date | None = None
    funding_amount: str | None = None
    fit_score: float | None = None
    status: str = "new"
    eligibility: str | None = None
    focus: str | None = None
    source_url: str | None = None
    notes: str | None = None
    client_id: int | None = None


class OpportunityRead(OpportunityCreate):
    id: int

    class Config:
        from_attributes = True

