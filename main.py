import time
from fetch_rates import get_eur_to_sek
from my_email import send_email
from logger_config import setup_logger

logger = setup_logger("SchedulerLogger")

def job():
    logger.info("Running scheduled job...")
    rate = get_eur_to_sek()
    send_email(rate)

job()