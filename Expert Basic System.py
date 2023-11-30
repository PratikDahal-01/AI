class ExpertSystem:
    def __init__(self):
        self.symptoms = set()
        self.rules = []

    def add_symptom(self, symptom):
        self.symptoms.add(symptom)

    def add_rule(self, symptoms, diagnosis):
        self.rules.append({"symptoms": set(symptoms), "diagnosis": diagnosis})

    def get_user_input(self):
        print("Enter symptoms separated by commas (e.g., fever, headache):")
        user_input = input().lower()
        return set(user_input.split(", "))

    def diagnose(self, user_symptoms):
        possible_diagnoses = []

        for rule in self.rules:
            if rule["symptoms"].issubset(user_symptoms):
                possible_diagnoses.append(rule["diagnosis"])

        return possible_diagnoses

    def run_diagnosis(self):
        print("Welcome to the Medical Expert System!")
        print("Available symptoms:", ", ".join(self.symptoms))

        user_symptoms = self.get_user_input()
        possible_diagnoses = self.diagnose(user_symptoms)

        if possible_diagnoses:
            print("Possible diagnoses:", ", ".join(possible_diagnoses))
        else:
            print("No matching diagnosis found.")

# Example Usage
expert_system = ExpertSystem()

# Define Symptoms
expert_system.add_symptom("fever")
expert_system.add_symptom("headache")
expert_system.add_symptom("cough")

# Define Rules
expert_system.add_rule(["fever", "headache"], "Common Cold")
expert_system.add_rule(["fever", "cough"], "Flu")
expert_system.add_rule(["headache", "cough"], "Migraine")

# Run Diagnosis
expert_system.run_diagnosis()

# Output:
# Welcome to the Medical Expert System!
# Available symptoms: headache, cough, fever
# Enter symptoms separated by commas (e.g., fever, headache):
# fever, headache
# Possible diagnoses: Common Cold