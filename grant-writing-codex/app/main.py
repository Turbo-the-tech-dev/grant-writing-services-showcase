from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.crud import create_opportunity, list_opportunities
from app.database import SessionLocal, init_db
from app.schemas import OpportunityCreate, OpportunityRead


app = FastAPI(title="Grant Writing Codex MVP")
init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/opportunities", response_model=list[OpportunityRead])
def get_opportunities(db: Session = Depends(get_db)):
    return list_opportunities(db)


@app.post("/opportunities", response_model=OpportunityRead)
def post_opportunity(payload: OpportunityCreate, db: Session = Depends(get_db)):
    return create_opportunity(db, payload)

