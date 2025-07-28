# prediction_helper.py

import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("artifacts/model_data.joblib")

# Sample mapping for label-encoded or one-hot encoded features
# Make sure to match with training preprocessing
def preprocess_input(input_dict):
    # Convert to DataFrame
    df = pd.DataFrame([input_dict])

    # Rename columns to match model expectations
    df.rename(columns={
        'Age': 'age',
        'Gender': 'gender',
        'Zone': 'zone',
        'Occupation': 'occupation',
        'Income Level (in L)': 'income_levels',
        'Consume Frequency(Weekly)': 'consume_frequency(weekly)',
        'Current Brand': 'current_brand',
        'Preferable Consumption Size': 'preferable_consumption_size',
        'Awareness of Other Brands': 'brand_awareness',
        'Preferable Consumption Size': 'reasons_for_choosing_brands',
        'Flavor Preference': 'flavor_preference',
        'Purchase Channel': 'purchase_channel',
        'Packaging Preference': 'packaging_preference',
        'Health Concerns': 'health_concerns',
        'Typical Consumption Situation': 'typical_consumption_situations'
    }, inplace=True)

    # Fill or encode values if required (e.g., one-hot or label encoding)
    # This step depends on what encoding the model was trained with
    # If the model expects encoded values, apply them here

    return df


# Predict function
def predict(input_dict):
    processed_df = preprocess_input(input_dict)
    prediction = model.predict(processed_df)[0]
    return prediction
