import os

import requests


title = "todoist-refresher-orchestrator"

TELEGRAM_SERVICE_URL = os.getenv("TELEGRAM_SERVICE_URL", "http://telegram-service:80")


def send_message_to_telegram(message: str):
    requests.post(
        TELEGRAM_SERVICE_URL + "/message", json={"message": message}
    )
    return {"message": "Message sent to telegram"}


def log_to_telegram(message: str, logging_function):
    logging_function(f"service: {title}, message: {message}")
    requests.post(
        TELEGRAM_SERVICE_URL + "/log",
        json={"service": title, "message": message},
    )
    return {"message": "Message sent to telegram"}
