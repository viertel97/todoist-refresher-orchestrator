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

ROUTER_NAME = "hourly"

def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "todoist_to_notion_routine"),
        CronTrigger.from_crontab("0 */1 * * *"),
        id="todoist_to_notion_routine",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "todoist_to_microjournal_routine"),
        CronTrigger.from_crontab("5 */1 * * *"),
        id="todoist_to_microjournal_routine",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "todoist_to_rethink_routine"),
        CronTrigger.from_crontab("10 */1 * * *"),
        id="todoist_to_rethink_routine",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "todoist_to_work_routine"),
        CronTrigger.from_crontab("15 */1 * * *"),
        id="todoist_to_work_routine",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "clean_inbox_activities_routine"),
        CronTrigger.from_crontab("40 */3 * * *"),
        id="clean_inbox_activities_routine",
    )
