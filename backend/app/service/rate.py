from datetime import datetime, timedelta
import requests 
from models import Rate


class RateService:
    """
    Pobranie kursu dla waluty z przedziału czasowego
    """
    @staticmethod
    def rates(currency: str, date_from: str, date_to: str) -> list|None:
        response = requests.get(
            f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_from}/{date_to}?format=json"
            )
        
        if response.status_code == 200:
            return list(map(lambda x: {"date": x['effectiveDate'], "rate": x['mid'] }, response.json()['rates']))
        
        return None


class RateServiceMigration:

    __MAX_API_DAY_RANGE = 93

    def __init__(self, db_session) -> None:
        self.db_session = db_session
    
    """
        Migracja kursu dla waluty.
        API NPB umozliwia pobranie jedynie maksymalnie 93-dniowego zakresu
        Migracja do bazy apliacji umozliwia wyswietlenie analizy dla dluzszych przedzialow czasu
    """
    def migrate(self, currency: str, date_from: str, date_to: str):
        
        start_date = datetime.strptime(date_from, "%Y-%m-%d")
        end_date = datetime.strptime(date_to, "%Y-%m-%d")
        delta = timedelta(days=self.__MAX_API_DAY_RANGE)

        current_date = start_date
        while current_date <= end_date:
            range_from = current_date.strftime("%Y-%m-%d")
            current_date += delta
            range_to = current_date.strftime("%Y-%m-%d")

            print(f"Requesting range: {range_from} - {range_to}")
            results = RateService.rates(currency, range_from, range_to)
            print(f"Results count {len(results)}")

            for result in results:
                rate_integer = int(result['rate'] * 1000)
                self.db_session.add(Rate(currency=currency, rate=rate_integer, rate_date=result['date']))
                self.db_session.commit()


    