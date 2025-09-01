import requests
from logger_config import setup_logger

logger = setup_logger("FetchRateLogger")

def get_eur_to_sek():
    """
    Fetch EUR → SEK conversion rate from Frankfurter API
    """
    try:
        url = "https://api.frankfurter.app/latest?from=EUR&to=SEK"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rate = data.get("rates", {}).get("SEK")

        if rate is None:
            logger.warning("EUR→SEK rate not found in API response")
            return None

        logger.info(f"Fetched EUR→SEK rate: {rate}")
        logger.debug(f"Full API response: {data}")
        return rate

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching EUR→SEK rate: {e}")
        return None
