# prediction_helper.py

import joblib                                                                                           # joblib: Loads the saved model.
import pandas as pd                                                                                     # pandas: Helps build a DataFrame for model input.
import numpy as np                                                                                      # numpy: Used for any numeric operations (not used here directly).



# Load the model                                                                                        # 🧠 2. Load the Trained ML Model
model_data = joblib.load("artifacts/model_data.joblib")                                                      # Loads a pre-trained model saved during the training phase.
model = model_data['model']

# Define the label encodings as per training phase                                                      # 🏷️ 3. Label Encoding Mappings
label_maps = {                                                                                          # Converts categorical string inputs (like gender, occupation, etc.) into numeric values used during training.
    'Gender': {'M': 0, 'F': 1},                                                                         # If label encoding isn't consistent with training, prediction will be wrong.
    'Zone': {'Rural': 0, 'Remi-Urban': 1, 'Urban': 2, 'Metro': 3},
    'Occupation': {'Working Professional': 0, 'Student': 1, 'Entrepreneur': 2, 'Retired': 3},

    'Income Level (in L)': {'<10L': 0, '10L-15L': 1, '16-25L': 2, '26-35L': 3, '>35L': 4},
    'Consume Frequency(Weekly)': {'0-2 times': 0, '3-4 times': 1, '5-7': 2},
    'Current Brand': {'Newcomer': 0, 'Established': 1},
    'Preferable Consumption Size': {'Small (250 ml)': 0, 'Medium (500ml)': 1, 'Large (1L)': 2},

    'Awareness of Other Brands': {'0 to 1': 0, '2 to 4': 1, 'above 4': 2},
    'Reasons for choosing brands': {'Price': 0, 'Quality': 1, 'Availability': 2, 'Brand Reputation': 3},
    'Flavor Preference': {'Traditional': 0, 'Exotic': 1},
    'Purchase Channel': {'Online': 0, 'Retail Store': 1},

    'Packaging Preference': {'Simple': 0, 'Premium': 1, 'Eco-Friendly': 2},
    'Health Concerns': {'Low (Not very concerned)': 0, 'Medium (Moderately health-conscious)': 1, 'High (Very health-conscious)': 2},
    'Typical Consumption Situation': {
        'Active (eg. Sports, gym)': 0,
        'Social (eg. Parties)': 1,
        'Casual (eg. At home)': 2
    }
}

def predict(input_dict):                                              # Takes a dictionary of user inputs as argument, e.g. from a form
    # Encode all inputs
    processed_input = {}                                              # 📦 4.1. Preprocess Inputs, Loops over all input fields.Encodes categorical values using label_maps
    for key, value in input_dict.items():                             # Leaves numeric fields (like Age) unchanged. Returns -1 if value is not found in encoding (acts as fallback).
        if key in label_maps: 
            processed_input[key] = label_maps[key].get(value, -1)
        else:
            processed_input[key] = value  # for numeric like Age

    # Convert to DataFrame with single row
    input_df = pd.DataFrame([processed_input])                        # Wraps the input dictionary into a single-row pandas DataFrame for prediction.

    # Predict
    prediction = model.predict(input_df)[0]                           # Uses the model to predict the output. Returns the predicted class (e.g., price range).

    if prediction == 0:
        return '50-100'
    elif prediction == 1:
        return '100-150'
    elif prediction == 2:
        return '150-200'
    elif prediction == 3:
        return '200-250'
