import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from evaluator.rule_based import rule_optimize
from evaluator.token_counter import count_tokens

prompt = "Please carefully explain the concept in a very detailed manner."

optimized = rule_optimize(prompt)

original_tokens = count_tokens(prompt)
optimized_tokens = count_tokens(optimized)

print("Original Prompt:", prompt)
print("Optimized Prompt:", optimized)
print("Original Tokens:", original_tokens)
print("Optimized Tokens:", optimized_tokens)
print("Token Reduction:", original_tokens - optimized_tokens)

