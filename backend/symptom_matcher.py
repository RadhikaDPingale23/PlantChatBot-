
# Symptom Matcher for Plant Disease ChatBot
#
# Uses Groq API for semantic symptom classification.

#from backend.groq_fallback import classify_symptoms_with_groq
from backend.groq_fallback import classify_symptoms_with_groq


def detect_crop(query: str) -> str:
    q = query.lower()

    if "tomato" in q:
        return "tomato"
    if "potato" in q:
        return "potato"
    if "pepper" in q or "chilli" in q:
        return "pepper"
    if "corn" in q or "maize" in q:
        return "corn"

    return "unknown"
def text_diagnosis(query: str) -> str:
    if not query or not query.strip():
        return "Unknown"

    q = query.lower()
    crop = detect_crop(q)

    # 🍅 TOMATO
    if crop == "tomato":
        if "yellow" in q and ("holes" in q or "spots" in q):
            return "Tomato___Leaf_Mold"
        if "brown" in q and "concentric" in q:
            return "Tomato___Early_Blight"
        if "black" in q and "white mold" in q:
            return "Tomato___Late_Blight"

    # 🥔 POTATO
    if crop == "potato":
        if "brown" in q and "spots" in q:
            return "Potato___Early_Blight"
        if "black" in q and ("rot" in q or "rotting" in q):
            return "Potato___Late_Blight"

    # 🌶 PEPPER
    if crop == "pepper":
        if "yellow" in q and ("curl" in q or "spots" in q):
            return "Pepper__bell___Bacterial_spot"

    return "Unknown"



def text_diagnosis_with_score(query: str) -> tuple:
    result = text_diagnosis(query)

    if result != "Unknown":
        return (result, 1)

    return ("Unknown", 0)
