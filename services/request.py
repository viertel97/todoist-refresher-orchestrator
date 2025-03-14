import os
import platform
import time

import requests as requests
from quarter_lib.logging import setup_logging

from proxies.telegram_proxy import log_to_telegram

logger = setup_logging(__file__)

IS_CONTAINER = os.getenv("IS_CONTAINER", "False") == "True"

if IS_CONTAINER:
    API_IP = "http://todoist-refresher-api.custom.svc.cluster.local:9100/"
else:
    IP = "localhost" if platform == "darwin" or platform == "win32" else "192.168.178.100"
    API_IP = "http://" + IP + ":9100/"

logger.info("API_IP: " + API_IP)

RETRIES = 5
WAIT_TIME = 10

def trigger_job(router, job_id):
    url = API_IP + router + "/" + job_id

    for attempt in range(RETRIES):
        try:
            logger.info(f"Attempting to trigger job of Router {router} with ID {job_id} at URL: {url}")
            response = requests.post(url)
            response.raise_for_status()  # Check if the request was successful
            try:
                result_json = response.json()
            except Exception as e:
                result_json = response
            logger.info(f"Positive response for URL {url} with content: {result_json}")
            if attempt > 0:
                log_to_telegram(f"Attempt for URL {url} was successful after {attempt} retries.", logger.info)
            return response.json()  # Return the response if successful
        except Exception as e:
            if attempt < RETRIES - 1:  # Only wait if there are retries left
                log_to_telegram(f"Attempt for URL {url} failed: {e}. Retrying in {WAIT_TIME} seconds.", logger.error)
                time.sleep(WAIT_TIME)
            else:
                log_to_telegram(f"Attempt for URL {url} failed: {e}. No more retries left.", logger.critical)