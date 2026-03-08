import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.features.feature_engineering import build_feature_dataset


def run_feature_pipeline():

    df = build_feature_dataset()

    print("\nFeature Dataset:\n")

    print(df.head())


if __name__ == "__main__":
    run_feature_pipeline()