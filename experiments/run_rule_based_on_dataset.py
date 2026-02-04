import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from evaluator.rule_based import rule_optimize
from evaluator.token_counter import count_tokens

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
INPUT_PATH = os.path.join(DATA_DIR, "raw_prompts.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "rule_based_results.csv")

def run_rule_based():
    df = pd.read_csv(INPUT_PATH)

    df["original_tokens"] = df["prompt"].apply(count_tokens)
    df["optimized_prompt"] = df["prompt"].apply(rule_optimize)
    df["optimized_tokens"] = df["optimized_prompt"].apply(count_tokens)
    df["token_reduction"] = df["original_tokens"] - df["optimized_tokens"]

    print("\nRule-Based Optimization Results:")
    print(df[["task", "original_tokens", "optimized_tokens", "token_reduction"]])

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved results to {OUTPUT_PATH}")

if __name__ == "__main__":
    run_rule_based()

