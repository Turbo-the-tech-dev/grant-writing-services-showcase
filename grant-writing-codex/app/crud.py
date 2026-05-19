from collections.abc import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import GrantOpportunity
from app.schemas import OpportunityCreate


def create_opportunity(db: Session, payload: OpportunityCreate) -> GrantOpportunity:
    record = GrantOpportunity(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def list_opportunities(db: Session) -> Iterable[GrantOpportunity]:
    stmt = select(GrantOpportunity).order_by(GrantOpportunity.deadline, GrantOpportunity.title)
    return db.scalars(stmt).all()


def gardena_high_fit_opportunities(db: Session, minimum_fit: float = 8.0) -> Iterable[GrantOpportunity]:
    stmt = (
        select(GrantOpportunity)
        .where(GrantOpportunity.fit_score >= minimum_fit)
        .where(GrantOpportunity.status.in_(["new", "researching", "drafting"]))
        .where(GrantOpportunity.focus.ilike("%small business%"))
        .order_by(GrantOpportunity.deadline)
    )
    return db.scalars(stmt).all()

