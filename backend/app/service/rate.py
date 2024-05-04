import requests


class RateService:

    @staticmethod
    def rates(currency: str, date_from: str, date_to: str) -> list|None:
        response = requests.get(
            f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_from}/{date_to}?format=json"
            )
        
        if response.status_code == 200:
            return list(map(lambda x: {"date": x['effectiveDate'], "rate": x['mid'] }, response.json()['rates']))
        
        return None
