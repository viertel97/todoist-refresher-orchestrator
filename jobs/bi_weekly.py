from apscheduler.triggers.cron import CronTrigger
from quarter_lib.logging import setup_logging
from services.request import trigger_job

logger = setup_logging(__name__)

ROUTER_NAME = "bi_weekly"


def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_book_rework"),
        CronTrigger.from_crontab("57 23 1,5,9,13,17,21,25,29 * *"),
        id="update_book_rework"
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_to_think_about"),
        CronTrigger.from_crontab("54 23 3,19 * *"),
        id="update_to_think_about",
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian_random_note"),
        CronTrigger.from_crontab("54 23 7,23 * *"),
        id="obsidian_random_note",
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian_oldest_note"),
        CronTrigger.from_crontab("54 23 11,27 * *"),
        id="obsidian_oldest_note",
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian_random_activity"),
        CronTrigger.from_crontab("54 23 15,31 * *"),
        id="obsidian_random_activity",
    )
