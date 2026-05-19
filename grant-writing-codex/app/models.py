from datetime import date, datetime

from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    city: Mapped[str | None] = mapped_column(String(120))
    state: Mapped[str | None] = mapped_column(String(50))
    sector: Mapped[str | None] = mapped_column(String(120))
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    opportunities: Mapped[list["GrantOpportunity"]] = relationship(back_populates="client")
    proposals: Mapped[list["Proposal"]] = relationship(back_populates="client")
    documents: Mapped[list["Document"]] = relationship(back_populates="client")


class GrantOpportunity(Base):
    __tablename__ = "grant_opportunities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int | None] = mapped_column(ForeignKey("clients.id"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    agency_name: Mapped[str | None] = mapped_column(String(255))
    date_received: Mapped[date | None] = mapped_column(Date)
    deadline: Mapped[date | None] = mapped_column(Date)
    funding_amount: Mapped[str | None] = mapped_column(String(120))
    fit_score: Mapped[float | None] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(80), default="new", nullable=False)
    eligibility: Mapped[str | None] = mapped_column(Text)
    focus: Mapped[str | None] = mapped_column(Text)
    source_url: Mapped[str | None] = mapped_column(String(500))
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    client: Mapped[Client | None] = relationship(back_populates="opportunities")
    proposals: Mapped[list["Proposal"]] = relationship(back_populates="opportunity")
    alerts: Mapped[list["PortalAlert"]] = relationship(back_populates="opportunity")


class Proposal(Base):
    __tablename__ = "proposals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    opportunity_id: Mapped[int] = mapped_column(ForeignKey("grant_opportunities.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    stage: Mapped[str] = mapped_column(String(80), default="draft", nullable=False)
    narrative_path: Mapped[str | None] = mapped_column(String(500))
    budget_path: Mapped[str | None] = mapped_column(String(500))
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    client: Mapped[Client] = relationship(back_populates="proposals")
    opportunity: Mapped[GrantOpportunity] = relationship(back_populates="proposals")


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    proposal_id: Mapped[int | None] = mapped_column(ForeignKey("proposals.id"))
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    doc_type: Mapped[str] = mapped_column(String(80), nullable=False)
    version: Mapped[str | None] = mapped_column(String(40))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    client: Mapped[Client] = relationship(back_populates="documents")


class PortalAlert(Base):
    __tablename__ = "portal_alerts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    opportunity_id: Mapped[int | None] = mapped_column(ForeignKey("grant_opportunities.id"))
    source_type: Mapped[str] = mapped_column(String(40), nullable=False)
    source_identifier: Mapped[str] = mapped_column(String(255), nullable=False)
    raw_subject: Mapped[str | None] = mapped_column(String(255))
    raw_payload: Mapped[str] = mapped_column(Text, nullable=False)
    received_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    opportunity: Mapped[GrantOpportunity | None] = relationship(back_populates="alerts")

