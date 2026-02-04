import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from evaluator.pipeline import optimize_prompt

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
INPUT_PATH = os.path.join(DATA_DIR, "expanded_prompts.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "final_results.csv")

def run_pipeline():
    df = pd.read_csv(INPUT_PATH)

    results = []
    for _, row in df.iterrows():
        res = optimize_prompt(row["prompt"])
        res["task"] = row["task"]
        results.append(res)

    result_df = pd.DataFrame(results)
    result_df.to_csv(OUTPUT_PATH, index=False)

    print("\nFinal Optimization Results:")
    print(result_df[["task", "original_tokens", "optimized_tokens", "token_reduction"]])
    print(f"\nSaved results to {OUTPUT_PATH}")

if __name__ == "__main__":
    run_pipeline()

