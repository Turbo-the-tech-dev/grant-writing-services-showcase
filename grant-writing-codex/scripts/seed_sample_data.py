from datetime import date, timedelta

from app.crud import create_opportunity
from app.database import SessionLocal, init_db
from app.schemas import OpportunityCreate


def main() -> None:
    init_db()
    sample_rows = [
        OpportunityCreate(
            title="Gardena Small Business Resilience Grant",
            agency_name="City of Gardena",
            date_received=date.today(),
            deadline=date.today() + timedelta(days=21),
            funding_amount="$25,000",
            fit_score=9.2,
            status="researching",
            focus="small business resilience and local economic development",
            eligibility="Gardena small businesses with less than 25 employees",
            notes="Sample seed record for dashboard testing.",
        ),
        OpportunityCreate(
            title="California Clean Transportation Planning Grant",
            agency_name="State of California",
            date_received=date.today(),
            deadline=date.today() + timedelta(days=45),
            funding_amount="$150,000",
            fit_score=7.4,
            status="new",
            focus="clean transportation planning",
            eligibility="Cities, nonprofits, and eligible partners",
        ),
    ]

    with SessionLocal() as db:
        for row in sample_rows:
            create_opportunity(db, row)


if __name__ == "__main__":
    main()

