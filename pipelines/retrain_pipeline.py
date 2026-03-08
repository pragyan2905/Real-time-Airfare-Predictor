import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apscheduler.schedulers.blocking import BlockingScheduler
from pipelines.full_pipeline import run_full_pipeline


def start_scheduler():

    scheduler = BlockingScheduler()

    # run pipeline every 6 hours
    scheduler.add_job(run_full_pipeline, "interval", hours=6)

    print("Automatic retraining scheduler started...")

    scheduler.start()


if __name__ == "__main__":
    start_scheduler()