from service.rate import RateServiceMigration
from database.database import get_db
from datetime import datetime
import argparse

"""
Migration rates to allow generating tables and charts for all period
"""
parser = argparse.ArgumentParser("CurrencyRateMigration")
parser.add_argument("currency", help="ISO code of currency", type=str)
parser.add_argument("date_from", help="date from", type=str, default="2002/01/01", required=False)
parser.add_argument("date_to", help="date to", type=str, required=False)
args = parser.parse_args()

session = next(get_db())

migration_service = RateServiceMigration(db_session=session)
migration_service.migrate(args.currency, args.date_from, datetime.now())



