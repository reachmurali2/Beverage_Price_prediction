# prediction_helper.py      WORKING code block

import joblib
import numpy as np
import pandas as pd

# Load the model and feature list
model_data = joblib.load("artifacts/model_data.joblib")
model = model_data["model"]
expected_columns = model_data["features"]

# Preprocessing function
def preprocess_input(input_dict):
    # Initialize DataFrame with all expected columns set to 0
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Label Encoded Columns
    zone_map = {'Rural': 1, 'Semi-Urban': 2, 'Urban': 3, 'Metro': 4}
    income_map = {'Not Reported': 0, '<10L': 1, '10L - 15L': 2, '16L - 25L': 3, '26L - 35L': 4, '> 35L': 5}
    freq_map = {'0-2 times': 1, '3-4 times': 2, '5-7 times': 3}
    size_map = {'Small (250 ml)': 1, 'Medium (500 ml)': 2, 'Large (1 L)': 3}
    aware_map = {'0 to 1': 1, '2 to 4': 2, 'above 4': 3}
    health_map = {
        'Low (Not very concerned)': 1,
        'Medium (Moderately health-conscious)': 2,
        'High (Very health-conscious)': 3
    }

    # Age Group Logic
    age = input_dict.get("Age", 0)
    if 18 <= age <= 25:
        age_group = 1
    elif 26 <= age <= 35:
        age_group = 2
    elif 36 <= age <= 45:
        age_group = 3
    elif 46 <= age <= 55:
        age_group = 4
    elif 56 <= age <= 70:
        age_group = 5
    else:
        age_group = 0

    # Label Encoded Columns
    df.at[0, 'zone'] = zone_map.get(input_dict.get('Zone'), 0)
    df.at[0, 'income_levels'] = income_map.get(input_dict.get('Income Level'), 0)
    df.at[0, 'consume_frequency(weekly)'] = freq_map.get(input_dict.get('Consume Frequency(Weekly)'), 0)
    df.at[0, 'preferable_consumption_size'] = size_map.get(input_dict.get('Preferable Consumption Size'), 0)
    df.at[0, 'awareness_of_other_brands'] = aware_map.get(input_dict.get('Awareness of other brands'), 0)
    df.at[0, 'health_concerns'] = health_map.get(input_dict.get('Health Concerns'), 0)
    df.at[0, 'age_group'] = age_group

    # One-Hot Encoded Columns (Set 1 if value matches)
    if input_dict.get('Gender') == 'M':
        df.at[0, 'gender_M'] = 1

    occ = input_dict.get('Occupation')
    if occ == 'Retired':
        df.at[0, 'occupation_Retired'] = 1
    elif occ == 'Student':
        df.at[0, 'occupation_Student'] = 1
    elif occ == 'Working Professional':
        df.at[0, 'occupation_Working Professional'] = 1

    if input_dict.get('Current Brand') == 'Newcomer':
        df.at[0, 'current_brand_Newcomer'] = 1

    reason = input_dict.get('Reasons for choosing brands')
    if reason == 'Brand Reputation':
        df.at[0, 'reasons_for_choosing_brands_Brand Reputation'] = 1
    elif reason == 'Price':
        df.at[0, 'reasons_for_choosing_brands_Price'] = 1
    elif reason == 'Quality':
        df.at[0, 'reasons_for_choosing_brands_Quality'] = 1

    if input_dict.get('Flavor Preference') == 'Traditional':
        df.at[0, 'flavor_preference_Traditional'] = 1

    if input_dict.get('Purchase Channel') == 'Retail Store':
        df.at[0, 'purchase_channel_Retail Store'] = 1

    pack = input_dict.get('Packaging Preference')
    if pack == 'Premium':
        df.at[0, 'packaging_preference_Premium'] = 1
    elif pack == 'Simple':
        df.at[0, 'packaging_preference_Simple'] = 1

    situation = input_dict.get('Typical Consumption Situations')
    if situation == 'Casual (eg. At home)':
        df.at[0, 'typical_consumption_situations_Casual (eg. At home)'] = 1
    elif situation == 'Social (eg. Parties)':
        df.at[0, 'typical_consumption_situations_Social (eg. Parties)'] = 1

    # Derived Features
    try:
        freq = df.at[0, 'consume_frequency(weekly)']
        aware = df.at[0, 'awareness_of_other_brands']
        df.at[0, 'cf_ab_score'] = round(freq / (freq + aware), 2) if (freq + aware) > 0 else 0
    except:
        df.at[0, 'cf_ab_score'] = 0

    df.at[0, 'zas_score'] = df.at[0, 'zone'] * df.at[0, 'income_levels']

    df.at[0, 'bsi'] = int(
        input_dict.get('Current Brand') != 'Established' and
        input_dict.get('Reasons for choosing brands') in ['Price', 'Quality']
    )

    return df


# Prediction Function
def predict(input_dict):
    input_df = preprocess_input(input_dict)
    pred = model.predict(input_df)[0]

    # Decode predicted label to original price range
    price_range_map = {
        0: '50-100',
        1: '100-150',
        2: '150-200',
        3: '200-250'
    }

    return price_range_map.get(pred, "Unknown")
