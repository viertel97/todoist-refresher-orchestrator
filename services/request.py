import platform

import requests as requests
from quarter_lib.logging import setup_logging

from services.telegram_service import send_to_telegram

logger = setup_logging(__file__)

IP = "localhost" if platform == "darwin" or platform == "win32" else "192.168.178.100"


def trigger_job(router, job_id):
    url = "http://" + IP + ":9100/" + router + "/" + job_id
    logger.info("trigger job: " + url)
    result = requests.post(url)
    if result.status_code != 200:
        logger.error("trigger job failed: " + str(result))
        send_to_telegram("trigger job (" + job_id + ") failed: " + str(result))
    else:
        logger.info("trigger job result: " + str(result))
