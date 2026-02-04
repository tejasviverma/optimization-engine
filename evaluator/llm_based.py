def llm_optimize(prompt: str) -> str:
    """
    MOCK version when API quota is unavailable.
    Simulates semantic compression.
    """
    replacements = {
        "please carefully": "",
        "in a very detailed manner": "",
        "in a detailed manner": "",
        "with explanation": "",
        "explain": "explain"
    }

    optimized = prompt.lower()
    for k, v in replacements.items():
        optimized = optimized.replace(k, v)

    optimized = " ".join(optimized.split())
    return optimized
