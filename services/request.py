import platform
import os
import requests as requests
from quarter_lib.logging import setup_logging

from services.telegram_service import send_to_telegram

logger = setup_logging(__file__)

IS_DOCKER = os.getenv("IS_DOCKER", "False") == "True"

if IS_DOCKER:
    API_IP = "http://todoist-refresher-api.default.svc.cluster.local:9100/"
else:
    IP = "localhost" if platform == "darwin" or platform == "win32" else "192.168.178.100"
    API_IP = "http://" + IP + ":9100/"

logger.info("API_IP: " + API_IP)

def trigger_job(router, job_id):
    url = API_IP + router + "/" + job_id
    logger.info("trigger job: " + url)
    result = requests.post(url)
    if result.status_code != 200:
        logger.error("trigger job failed: " + str(result))
        send_to_telegram("trigger job (" + job_id + ") failed: " + str(result))
    else:
        logger.info("trigger job result: " + str(result))
