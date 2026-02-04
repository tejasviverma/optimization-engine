import pandas as pd
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

INPUT_PATH = os.path.join(DATA_DIR, "raw_prompts.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "expanded_prompts.csv")

PREFIXES = [
    "Please carefully",
    "Kindly",
    "In a very detailed manner, please",
    "With proper explanation,"
]

SUFFIXES = [
    "with detailed explanation.",
    "while maintaining clarity.",
    "and explain each step carefully.",
    "with all necessary details."
]

def expand_dataset():
    df = pd.read_csv(INPUT_PATH)
    expanded_rows = []

    for idx, row in df.iterrows():
        expanded_rows.append(row.to_dict())

        for i, prefix in enumerate(PREFIXES):
            new_prompt = f"{prefix} {row['prompt']} {SUFFIXES[i % len(SUFFIXES)]}"
            expanded_rows.append({
                "id": f"{row['id']}_exp{i}",
                "task": row["task"],
                "prompt": new_prompt
            })

    expanded_df = pd.DataFrame(expanded_rows)
    expanded_df.to_csv(OUTPUT_PATH, index=False)

    print("Dataset expansion complete")
    print(f"Original size: {len(df)}")
    print(f"Expanded size: {len(expanded_df)}")

if __name__ == "__main__":
    expand_dataset()

