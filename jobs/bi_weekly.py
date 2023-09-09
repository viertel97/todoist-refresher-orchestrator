from apscheduler.triggers.cron import CronTrigger
from quarter_lib.logging import setup_logging
from services.request import trigger_job

logger = setup_logging(__name__)

ROUTER_NAME = "bi_weekly"


def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_to_think_about"),
        CronTrigger.from_crontab("54 23 2/10 * *"),
        id="update_to_think_about",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian_random_note"),
        CronTrigger.from_crontab("54 23 4/10 * *"),
        id="obsidian_random_note",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian_random_activity"),
        CronTrigger.from_crontab("54 23 6/10 * *"),
        id="obsidian_random_activity",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "obsidian_oldest_note"),
        CronTrigger.from_crontab("54 23 8/10 * *"),
        id="obsidian_oldest_note",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_book_rework"),
        CronTrigger.from_crontab("57 23 10/10 * *"),
        id="update_book_rework"
    )
