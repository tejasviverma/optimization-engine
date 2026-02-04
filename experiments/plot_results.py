import os
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
INPUT_PATH = os.path.join(DATA_DIR, "final_results.csv")

df = pd.read_csv(INPUT_PATH)

plt.figure()
plt.bar(df.index, df["token_reduction"])
plt.xlabel("Prompt Index")
plt.ylabel("Token Reduction")
plt.title("Token Reduction Across Prompts")
plt.show()


