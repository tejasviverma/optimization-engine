import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from evaluator.pipeline import optimize_prompt

prompt = "Please carefully explain the concept in a very detailed manner."

result = optimize_prompt(prompt)

print("Original Prompt:", result["original_prompt"])
print("Optimized Prompt:", result["optimized_prompt"])
print("Original Tokens:", result["original_tokens"])
print("Optimized Tokens:", result["optimized_tokens"])
print("Token Reduction:", result["token_reduction"])

