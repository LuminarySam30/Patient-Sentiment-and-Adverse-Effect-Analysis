def genai(initial):
    # Mock response for when API key is missing
    print(f"DEBUG: GenAI called with prompt: {initial[:50]}...")
    if "side effects" in initial.lower():
        return "*Nausea*Headache*Dizziness*Fatigue*"
    elif "reviews" in initial.lower():
        return "This medication helped me a lot, but I felt a bit dizzy. Overall good experience."
    else:
        return "*Mock Data 1*Mock Data 2*Mock Data 3*"
