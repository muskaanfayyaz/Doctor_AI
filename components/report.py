import streamlit as st
from googletrans import Translator

class DiagnosisReport:
    def __init__(self, patient, diagnosis_result, language):
        self.patient = patient
        self.diagnosis_result = diagnosis_result
        self.language = language
        self.translator = Translator()

    def display(self):
        # Translate the fields if needed
        st.subheader("Diagnosis Report")
        
        name = self.translate_text(self.patient.name)
        age = f"{self.patient.age} years old"
        date = self.patient.date
        symptoms = self.translate_text(self.patient.symptoms)
        diagnosis = self.translate_text(', '.join(self.diagnosis_result))

        st.write(f"👤 Name: {name}")
        st.write(f"🎂 Age: {age}")
        st.write(f"🕒 Date: {date}")
        st.write(f"📝 Symptoms: {symptoms}")

        if isinstance(self.diagnosis_result, list):
            st.write("🤖 AI Diagnostic Suggestions:")
            for label in self.diagnosis_result:
                st.write(f"- {label}")
        else:
            st.error(self.diagnosis_result)

    def translate_text(self, text):
        try:
            translated = self.translator.translate(text, src='en', dest=self.language)
            return translated.text
        except Exception as e:
            return f"Translation error: {str(e)}"
