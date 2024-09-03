import requests


title = "todoist-refresher-orchestrator"


def send_message_to_telegram(message: str):
    requests.post(
        "http://telegram-service.custom.svc.cluster.local:80/message", json={"message": message}
    )
    return {"message": "Message sent to telegram"}


def log_to_telegram(message: str, logging_function):
    logging_function(f"service: {title}, message: {message}")
    requests.post(
        "http://telegram-service.custom.svc.cluster.local:80/log",
        json={"service": title, "message": message},
    )
    return {"message": "Message sent to telegram"}
