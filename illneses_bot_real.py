import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics

class IllnessChatbot:
    def __init__(self):
        self.data = pd.read_csv('illness_data_extended.csv')
        self.X_train, self.X_test, self.y_train, self.y_test = self.prepare_data()
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())

    def prepare_data(self):
        X = self.data['Symptoms']
        y = self.data['Illness']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_classifier(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate_classifier(self):
        y_pred = self.model.predict(self.X_test)
        accuracy = metrics.accuracy_score(self.y_test, y_pred)
        print(f'Model Accuracy: {accuracy:.2f}')

    def identify_illness(self, symptoms):
        symptoms_text = ' '.join(symptoms)
        predicted_illness = self.model.predict([symptoms_text])
        return predicted_illness[0]

    def get_illness_info(self, illness):
        # Assume that the information is available in a dictionary or DataFrame
        # This needs to be adapted based on the actual structure of your data
        illness_info = {
            'Chicken pox': {
                'Incubation': '10-21 days',
                'Communicability': 'Thru inhalation of airborne droplets & direct contact of weeping lesions & contaminated linens.',
                'Prevention': 'Mask patient. Provider should avoid contact if they’ve never had chicken pox. Vaccination now available (1995) and part of childhood immunizations. Pt isolated until all lesions crusted over and dry.'
            },
            'Common cold': {
                'Incubation': '12 hours – 5 days (average 48 hours)',
                'Communicability': 'Direct contact, airborne droplet, contaminated hands and linens.',
                'Prevention': 'Handwashing'
            },
            # Add more illnesses and information as needed
        }

        return illness_info.get(illness, {})

# Example of using the chatbot
if __name__ == "__main__":
    chatbot = IllnessChatbot()
    chatbot.train_classifier()
    chatbot.evaluate_classifier()  # Optional: Evaluate the model accuracy

    # Simulate user input
    user_input = input("Enter your symptoms (space-separated): ")
    user_symptoms = user_input.split()

    # Identify the illness based on symptoms
    identified_illness = chatbot.identify_illness(user_symptoms)

    if identified_illness:
        print("Predicted illness: ", identified_illness)
        illness_info = chatbot.get_illness_info(identified_illness)
        if illness_info:
            print("\nIncubation:", illness_info['Incubation'])
            print("Communicability:", illness_info['Communicability'])
            print("Prevention:", illness_info['Prevention'])
        else:
            print("No information available for the identified illness.")
    else:
        print("No matching illnesses found.")
