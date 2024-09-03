import platform
import os
import requests as requests
from quarter_lib.logging import setup_logging
import time
from services.telegram_service import send_to_telegram

logger = setup_logging(__file__)

IS_CONTAINER = os.getenv("IS_CONTAINER", "False") == "True"

if IS_CONTAINER:
    API_IP = "http://todoist-refresher-api.custom.svc.cluster.local:9100/"
else:
    IP = "localhost" if platform == "darwin" or platform == "win32" else "192.168.178.100"
    API_IP = "http://" + IP + ":9100/"

logger.info("API_IP: " + API_IP)

RETRIES = 5
WAIT_TIME = 2

def trigger_job(router, job_id):
    url = API_IP + router + "/" + job_id

    for attempt in range(RETRIES):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            # try to get json from response, otherwise log result object
            try:
                result_json = response.json()
            except Exception as e:
                result_json = response
            logger.info(f"Response for URL {url}: {result_json}")
            return response.json()  # Return the response if successful
        except requests.exceptions.RequestException as e:
            if attempt < RETRIES - 1:  # Only wait if there are retries left
                logger.error(f"Attempt for URL {url} failed: {e}. Retrying in {WAIT_TIME} seconds.")
                send_to_telegram(f"Attempt for URL {url} failed: {e}. Retrying in {WAIT_TIME} seconds.")
                time.sleep(WAIT_TIME)
            else:
                send_to_telegram(f"Attempt for URL {url} failed: {e}. No more retries left.")
                logger.error(f"Attempt for URL {url} failed: {e}. No more retries left.")