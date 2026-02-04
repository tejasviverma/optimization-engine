from evaluator.rule_based import rule_optimize
from evaluator.llm_based import llm_optimize
from evaluator.token_counter import count_tokens

def optimize_prompt(prompt: str) -> dict:
    """
    End-to-end prompt optimization pipeline.
    """

    original_tokens = count_tokens(prompt)

    rule_prompt = rule_optimize(prompt)
    llm_prompt = llm_optimize(rule_prompt)

    optimized_tokens = count_tokens(llm_prompt)

    return {
        "original_prompt": prompt,
        "optimized_prompt": llm_prompt,
        "original_tokens": original_tokens,
        "optimized_tokens": optimized_tokens,
        "token_reduction": original_tokens - optimized_tokens
    }

