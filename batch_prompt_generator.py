
import random
import pandas as pd

NATIONALITIES = ["Asian", "African", "Caucasian", "Latino", "Middle Eastern", "Mixed Ethnicity"]
BACKGROUNDS = ["studio seamless", "minimal interior", "urban rooftop", "beachfront", "luxury hotel lobby"]
STYLES = ["editorial chic", "modern minimalist", "elevated casual", "high fashion", "classic elegance"]
LIGHTINGS = ["soft directional lighting", "moody shadows", "golden hour", "studio flash", "natural diffused"]
SHOT_SIZES = ["close-up", "medium shot", "full body", "three-quarter"]
GENDERS = ["female", "male", "androgynous"]
REFERENCES = {
    "skincare": ["https://www.vogue.com/editorial/spring2025", "https://www.behance.net/gallery/skincare-clean-retouch"],
    "fashion": ["https://www.behance.net/gallery/fashion-portrait-studio", "https://pinterest.com/editorial2025"],
    "business": ["https://www.behance.net/gallery/business-portrait-lighting"],
    "lifestyle": ["https://pinterest.com/lifestyleeditorial2025"]
}

def generate_prompt(concept, nationality, background, style, lighting, shot_size, gender):
    return (
        f"{concept}. {shot_size.capitalize()} portrait of a {gender} model of {nationality} descent, styled in {style}. "
        f"Photographed against a {background} background with {lighting}. This editorial-style composition is crafted for commercial use, ideal for brand storytelling, product integration, and visual campaigns."
    )

def generate_metadata(prompt, category):
    title = prompt.split(".")[0][:70].strip()
    keywords = ["editorial", "fashion", "branding", "commercial", "2025", category.lower()]
    keywords = sorted(set(keywords))
    description = (
        f"Professionally captured editorial portrait created for {category.lower()} and commercial applications. "
        f"Designed with attention to detail in lighting, background, and styling, making it ideal for premium stock usage, brand campaigns, and marketing visuals."
    )
    return title, ", ".join(keywords), description

def suggest_improvements(prompt):
    suggestions = []
    if "negative space" not in prompt:
        suggestions.append("Consider adding 'negative space' for flexible product placement.")
    if "color palette" not in prompt:
        suggestions.append("You could specify a 'color palette' to control visual tone.")
    if "mood" not in prompt:
        suggestions.append("Think about adding a 'mood' like calm, bold, or confident.")
    return suggestions

def generate_batch(concepts, category, batch_size=10):
    data = []
    for _ in range(batch_size):
        concept = random.choice(concepts)
        theme = "fashion"
        if "skincare" in concept.lower():
            theme = "skincare"
        elif "business" in concept.lower():
            theme = "business"
        elif "wellness" in concept.lower():
            theme = "lifestyle"

        nationality = random.choice(NATIONALITIES)
        background = random.choice(BACKGROUNDS)
        style = random.choice(STYLES)
        lighting = random.choice(LIGHTINGS)
        shot_size = random.choice(SHOT_SIZES)
        gender = random.choice(GENDERS)
        reference = random.choice(REFERENCES.get(theme, []))

        prompt = generate_prompt(concept, nationality, background, style, lighting, shot_size, gender)
        title, keywords, description = generate_metadata(prompt, category)
        suggestions = suggest_improvements(prompt)

        data.append({
            "Title": title,
            "Prompt": prompt,
            "Keywords": keywords,
            "Image Description": description,
            "Suggestions": " | ".join(suggestions),
            "Category": category,
            "Nationality": nationality,
            "Background": background,
            "Style": style,
            "Lighting": lighting,
            "Shot Size": shot_size,
            "Gender": gender,
            "Reference": reference
        })

    return pd.DataFrame(data)
