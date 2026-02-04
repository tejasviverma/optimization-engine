import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from evaluator.llm_based import llm_optimize
from evaluator.token_counter import count_tokens

prompt = "Please carefully explain the concept in a very detailed manner."

optimized = llm_optimize(prompt)

print("Original Prompt:")
print(prompt)
print("\nOptimized Prompt:")
print(optimized)

print("\nOriginal Tokens:", count_tokens(prompt))
print("Optimized Tokens:", count_tokens(optimized))
print("Token Reduction:", count_tokens(prompt) - count_tokens(optimized))

