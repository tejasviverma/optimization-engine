import os
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
INPUT_PATH = os.path.join(DATA_DIR, "final_results.csv")

def analyze():
    df = pd.read_csv(INPUT_PATH)

    # Summary table
    summary = df.groupby("task")[[
        "original_tokens",
        "optimized_tokens",
        "token_reduction"
    ]].mean().reset_index()

    print("\n=== Average Results by Task ===")
    print(summary)

    # Overall stats
    print("\n=== Overall Statistics ===")
    print(df[["original_tokens", "optimized_tokens", "token_reduction"]].describe())

if __name__ == "__main__":
    analyze()

