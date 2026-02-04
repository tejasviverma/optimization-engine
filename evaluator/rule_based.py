def rule_optimize(prompt: str) -> str:
    """
    Applies simple deterministic rules to remove verbosity
    without changing semantic intent.
    """
    rules = {
        "please": "",
        "carefully": "",
        "in a detailed manner": "",
        "in a very detailed manner": "",
        "in a clear and concise manner": "clearly",
        "with explanation": "",
        "with proper explanation": ""
    }

    optimized = prompt.lower()

    for phrase, replacement in rules.items():
        optimized = optimized.replace(phrase, replacement)

    # Clean extra spaces
    optimized = " ".join(optimized.split())

    return optimized

