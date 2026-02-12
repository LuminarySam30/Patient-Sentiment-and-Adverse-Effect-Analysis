def genai(initial):
    # Mock response for when API key is missing
    print(f"DEBUG: GenAI called with prompt: {initial[:50]}...")
    low_prompt = initial.lower()
    if "side effects" in low_prompt and "diet" in low_prompt:
        return "*Eat small, frequent meals to reduce nausea.*Stay hydrated by drinking at least 8 glasses of water.*Avoid spicy and greasy foods.*Incorporate ginger tea for stomach soothing.*Rest in a cool, dark room if headaches persist."
    elif "side effects" in low_prompt:
        return "*Nausea*Headache*Dizziness*Fatigue*"
    elif "reviews" in low_prompt:
        return "This medication helped me a lot, but I felt a bit dizzy. Overall good experience."
    elif "explanation" in low_prompt or "diagnosis" in low_prompt:
        return "*Symptoms Analysis: The reported symptoms align with clinical presentations of the predicted condition.*Risk Factors: Environmental factors or recent exposure may have contributed.*Recommendation: Clinical evaluation is required to confirm this diagnosis and rule out other possibilities.*"
    else:
        return "*Maintain a balanced diet.*Consult your doctor for specific advice.*Monitor your symptoms daily.*"
