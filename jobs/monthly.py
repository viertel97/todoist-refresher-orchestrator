from apscheduler.triggers.cron import CronTrigger
from quarter_lib.logging import setup_logging

from services.request import trigger_job

logger = setup_logging(__name__)

ROUTER_NAME = "monthly"


def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "whole_book_routine"),
        CronTrigger.from_crontab("0 3 1 * *"),
        id="whole_book_routine"
    )