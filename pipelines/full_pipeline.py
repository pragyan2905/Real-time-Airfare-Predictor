import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipelines.data_pipeline import run_pipeline
from pipelines.feature_pipeline import run_feature_pipeline
from src.training.train_model import run_training_pipeline


def run_full_pipeline():

    print("\nStep 1: Collecting new flight data...")
    run_pipeline()

    print("\nStep 2: Generating features...")
    run_feature_pipeline()

    print("\nStep 3: Training model...")
    run_training_pipeline()

    print("\nFull pipeline completed successfully.")


if __name__ == "__main__":
    run_full_pipeline()