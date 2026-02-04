import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from evaluator.token_counter import count_tokens

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
INPUT_PATH = os.path.join(DATA_DIR, "raw_prompts.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "baseline_stats.csv")

def run_baseline():
    df = pd.read_csv(INPUT_PATH)
    df["token_count"] = df["prompt"].apply(count_tokens)

    print("\nBaseline Token Statistics")
    print(df[["task", "token_count"]])

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved baseline stats to {OUTPUT_PATH}")

if __name__ == "__main__":
    run_baseline()

