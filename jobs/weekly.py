import os

from apscheduler.triggers.cron import CronTrigger
from loguru import logger

from services.request import trigger_job

logger.add(
    os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/logs/" + os.path.basename(__file__) + ".log"),
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    backtrace=True,
    diagnose=True,
)

ROUTER_NAME = "weekly"


def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_todoist_projects"),
        CronTrigger.from_crontab("3 19 * * sun"),
        id="update_todoist_projects",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "tpt"),
        CronTrigger.from_crontab("0 19 * * sun"),
        id="tpt",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "mm"),
        CronTrigger.from_crontab("10 19 * * sun"),
        id="mm",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "ght_update"),
        CronTrigger.from_crontab("58 23 * * sun"),
        id="ght_update",
    )

    scheduler.remove_job("tpt")
    scheduler.remove_job("mm")

