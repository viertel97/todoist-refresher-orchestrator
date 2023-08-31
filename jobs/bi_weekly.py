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

ROUTER_NAME = "bi_weekly"


def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_to_think_about"),
        CronTrigger.from_crontab("54 23 1/3 * *"),
        id="update_to_think_about",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian"),
        CronTrigger.from_crontab("54 23 2/3 * *"),
        id="obsidian",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_book_rework"),
        CronTrigger.from_crontab("57 23 3/3 * *"),
        id="update_book_rework"
    )
