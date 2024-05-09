from service.rate import RateServiceMigration
from database.database import get_db
from datetime import datetime

session = next(get_db())

migration_service = RateServiceMigration(db_session=session)
migration_service.migrate('EUR', datetime(2002, 1, 1), datetime.now())



