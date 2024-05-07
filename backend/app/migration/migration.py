from service.rate import RateServiceMigration
from backend.app.database.database import get_db

session = next(get_db())

migration_service = RateServiceMigration(db_session=session)
migration_service.migrate('USD', '2002-01-01', '2024-05-06')



