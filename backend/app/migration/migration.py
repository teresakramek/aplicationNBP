from service.rate import RateServiceMigration
from database.database import get_db

session = get_db()

migration_service = RateServiceMigration(db_session=session)
migration_service.migrate('EUR', '2002-01-01', '2024-05-06')



