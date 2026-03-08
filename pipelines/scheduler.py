import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apscheduler.schedulers.blocking import BlockingScheduler
from pipelines.data_pipeline import run_pipeline


scheduler = BlockingScheduler()

# Run every 3 hours
#scheduler.add_job(run_pipeline, "interval", hours=3)
scheduler.add_job(run_pipeline, "interval", seconds=10)

print("Scheduler started. Collecting flight data every 3 hours.")

scheduler.start()