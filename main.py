import streamlit as st
from components.voice_assistant import VoiceAssistant
from components.patient import Patient
from components.ai_doctor import AIDoctorAssistant
from components.report import DiagnosisReport
from utils.voice_input import get_voice_input

def main():
    st.set_page_config(page_title="AI Doctor Assistant", page_icon="🧠")
    st.title("🧠 AI Doctor Assistant (Multilingual + Voice + Smart)")
    st.markdown("Describe your symptoms in any language and get AI-based diagnostic suggestions.")

    assistant = AIDoctorAssistant()
    speaker = VoiceAssistant()

    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=1, max_value=120)
    language = st.selectbox("Language of Description", ['en', 'ur', 'hi', 'fr', 'es', 'zh-cn', 'ar', 'de'])
    use_voice = st.checkbox("Use Voice Input")

    if use_voice:
        if st.button("Record Now"):
            symptoms = get_voice_input()
            st.success(f"You said: {symptoms}")
    else:
        symptoms = st.text_area("Describe your symptoms here:")

    if st.button("Diagnose Me") and symptoms:
        patient = Patient(name=name, age=age, symptoms=symptoms, language=language)
        translated = assistant.translate_to_english(patient.symptoms, patient.language)

        if "Translation error" in translated:
            st.error(translated)
            return

        diagnosis = assistant.diagnose(translated)

        if diagnosis:
            report = DiagnosisReport(patient, diagnosis, language)
            report.display()

            speaker.speak(f"Hello {name}, I found some possible conditions.")
            for result in diagnosis:
                speaker.speak(f"{result['label']} with {round(result['score']*100)} percent confidence")

    elif symptoms == "":
        st.warning("Please enter or speak your symptoms before diagnosing.")
    else:
        st.error("Something went wrong. Please try again.")

if __name__ == "__main__":
    main()
