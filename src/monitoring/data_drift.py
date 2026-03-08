from evidently.report import Report
from evidently.metrics import DataDriftPreset
import pandas as pd

def run_drift(reference_data, current_data):

    report = Report(metrics=[DataDriftPreset()])

    report.run(
        reference_data=reference_data,
        current_data=current_data
    )

    report.save_html("monitoring/data_drift_report.html")