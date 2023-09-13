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

ROUTER_NAME = "daily"


def add_jobs(scheduler):
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "monica-morning"),
        CronTrigger.from_crontab("0 7 * * *"),
        id="monica-morning",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "monica-evening"),
        CronTrigger.from_crontab("50 23 * * *"),
        id="monica-evening",
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "monica_before_tasks/1"),
        CronTrigger.from_crontab("55 23 * * *"),
        id="monica_for_following_days",
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_monica_archive"),
        CronTrigger.from_crontab("45 23 * * *"),
        id="update_monica_archive",

    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "update_notion_habit_tracker"),
        CronTrigger.from_crontab("0 7 * * *"),
        id="update_notion_habit_tracker",
    )

    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "vacation_mode_checker"),
        CronTrigger.from_crontab("0 23 * * *"),
        id="vacation_mode_checker",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "notion_habit_tracker_stack"),
        CronTrigger.from_crontab("5 23 * * *"),
        id="notion_habit_tracker_stack",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "stretch_tpt"),
        CronTrigger.from_crontab("5 1 * * *"),
        id="stretch_tpt",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "stretch_articles"),
        CronTrigger.from_crontab("10 1 * * *"),
        id="stretch_articles",
    )
    scheduler.add_job(
        lambda: trigger_job(ROUTER_NAME, "article_to_audio_routine"),
        CronTrigger.from_crontab("0 2 * * *"),
        id="article_to_audio_routine",
    )