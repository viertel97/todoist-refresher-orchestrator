from sys import platform

from apscheduler.schedulers.blocking import BlockingScheduler
from quarter_lib.logging import setup_logging

from jobs.all_jobs import add_all_jobs
from services.request import trigger_job


logger = setup_logging(__file__)


def main():
    logger.info("Platform: " + str(platform))
    if not(platform == "darwin" or platform == "win32"):
        trigger_job("hourly", "clean_inbox_activities_routine")
        logger.info("test")
    else:
        scheduler = BlockingScheduler(timezone="Europe/Berlin")
        logger.info("Timezone: " + str(scheduler.timezone))
        scheduler = add_all_jobs(scheduler)

        logger.info("jobs: \n")
        jobs = scheduler.get_jobs()
        for job in jobs:
            logger.info("    %s" % job)
        logger.info("start scheduler")
        scheduler.start()


if __name__ == "__main__":
    main()
