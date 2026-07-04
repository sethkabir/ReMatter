from ollama import chat


def classify_material(description, image_base64=None):
    prompt = f"""You are a materials classification expert for an industrial
circularity platform. Given this material description: "{description}"

Return ONLY valid JSON with these keys:
- material_type: specific classification (e.g. "chrome-tanned upholstery-grade leather")
- category: one of [leather, textile, food_agri_byproduct]
- confidence: 0-1
- reuse_applications: list of 3-5 specific (not generic) reuse applications
"""
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are an expert materials classification assistant. Always return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.message.content