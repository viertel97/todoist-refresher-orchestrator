from jobs.bi_weekly import add_jobs as add_bi_weekly_jobs
from jobs.daily import add_jobs as add_daily_jobs
from jobs.hourly import add_jobs as add_hourly_jobs
from jobs.weekly import add_jobs as add_weekly_jobs


def add_all_jobs(scheduler):
    add_hourly_jobs(scheduler)
    add_daily_jobs(scheduler)
    add_bi_weekly_jobs(scheduler)
    add_weekly_jobs(scheduler)
    # add_bi_monthly_jobs(schedule)
    return scheduler
