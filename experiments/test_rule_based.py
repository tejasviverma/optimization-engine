import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from evaluator.rule_based import rule_optimize

prompt = "Please carefully explain the concept in a very detailed manner."
optimized = rule_optimize(prompt)

print("Original:", prompt)
print("Optimized:", optimized)
