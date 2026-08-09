# Backend module for Plant Disease ChatBot
# Re-exports from internal modules

from .chatbot import *
from .voice_handler import transcribe_audio
from .symptom_matcher import text_diagnosis

# Import from knowledge layer
from knowledge import get_treatment, format_treatment_response, get_uncertain_response

# ---- NOTE ----
# Do NOT import process_voice_input from app.py
# to avoid circular imports. process_voice_input should remain in backend/voice_handler.py
