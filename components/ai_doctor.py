from googletrans import Translator
from transformers import pipeline

class AIDoctorAssistant:
    def __init__(self):
        self.translator = Translator()
        self.model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def translate_to_english(self, text: str, src_lang: str):
        if src_lang.lower() == 'en':
            return text
        try:
            # Translate the symptoms to English
            translated = self.translator.translate(text, src=src_lang, dest='en')
            return translated.text
        except Exception as e:
            return f"Translation error: {str(e)}"

    def diagnose(self, english_text: str):
        try:
            labels = ['flu', 'cold', 'fever', 'headache', 'stomach ache', 'cough', 'allergy']
            result = self.model(english_text, candidate_labels=labels)
            return result['labels']
        except Exception as e:
            return [{"label": "error", "score": str(e)}]
