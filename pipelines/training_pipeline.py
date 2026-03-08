import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.training.train_model import run_training_pipeline


if __name__ == "__main__":
    run_training_pipeline()