import datetime

class Patient:
    def __init__(self, name: str, age: int, symptoms: str, language: str = "en"):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.language = language
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_patient_history(self):
        # This can later be enhanced to fetch from a database
        return f"{self.name} ({self.age} years old), Symptoms: {self.symptoms}, Date: {self.date}"
