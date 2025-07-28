# prediction_helper40.py

import joblib
import pandas as pd

# Load model and features
model_data = joblib.load("artifacts/model_data.joblib")
model = model_data["model"]
# expected_columns = model_data["features"]


# Mappings
LABEL_MAPS = {
    'Zone': {'Rural': 1, 'Semi-Urban': 2, 'Urban': 3, 'Metro': 4},
    'Income Level': {'Not Reported': 0, '<10L': 1, '10L - 15L': 2, '16L - 25L': 3, '26L - 35L': 4, '> 35L': 5},
    'Consume Frequency(Weekly)': {'0-2 times': 1, '3-4 times': 2, '5-7 times': 3},
    'Preferable Consumption Size': {'Small (250 ml)': 1, 'Medium (500 ml)': 2, 'Large (1 L)': 3},
    'Awareness of other brands': {'0 to 1': 1, '2 to 4': 2, 'above 4': 3},
    'Health Concerns': {
        'Low (Not very concerned)': 1,
        'Medium (Moderately health-conscious)': 2,
        'High (Very health-conscious)': 3
    }
}

ONE_HOT_KEYS = {
    'Gender': {'M': 'gender_M'},
    'Occupation': {
        'Retired': 'occupation_Retired',
        'Student': 'occupation_Student',
        'Working Professional': 'occupation_Working Professional'
    },
    'Current Brand': {'Newcomer': 'current_brand_Newcomer'},
    'Reasons for choosing brands': {
        'Brand Reputation': 'reasons_for_choosing_brands_Brand Reputation',
        'Price': 'reasons_for_choosing_brands_Price',
        'Quality': 'reasons_for_choosing_brands_Quality'
    },
    'Flavor Preference': {'Traditional': 'flavor_preference_Traditional'},
    'Purchase Channel': {'Retail Store': 'purchase_channel_Retail Store'},
    'Packaging Preference': {
        'Premium': 'packaging_preference_Premium',
        'Simple': 'packaging_preference_Simple'
    },
    'Typical Consumption Situations': {
        'Casual (eg. At home)': 'typical_consumption_situations_Casual (eg. At home)',
        'Social (eg. Parties)': 'typical_consumption_situations_Social (eg. Parties)'
    }
}

PRICE_MAP = {0: '50-100', 1: '100-150', 2: '150-200', 3: '200-250'}

def encode_age(age):
    if 18 <= age <= 25:
        return 1
    elif 26 <= age <= 35:
        return 2
    elif 36 <= age <= 45:
        return 3
    elif 46 <= age <= 55:
        return 4
    elif 56 <= age <= 70:
        return 5
    return 0

def preprocess_input(input_dict):
    expected_columns = [                                                     # X_train.columns
        'zone', 'income_levels', 'consume_frequency(weekly)',
       'preferable_consumption_size', 'awareness_of_other_brands',
       'health_concerns', 'age_group', 'cf_ab_score', 'zas_score', 'bsi',
       'gender_M', 'occupation_Retired', 'occupation_Student',
       'occupation_Working Professional', 'current_brand_Newcomer',
       'reasons_for_choosing_brands_Brand Reputation',
       'reasons_for_choosing_brands_Price',
       'reasons_for_choosing_brands_Quality', 'flavor_preference_Traditional',
       'purchase_channel_Retail Store', 'packaging_preference_Premium',
       'packaging_preference_Simple',
       'typical_consumption_situations_Casual (eg. At home)',
       'typical_consumption_situations_Social (eg. Parties)'
    ]
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Label encoding
    for key, mapping in LABEL_MAPS.items():
        df.at[0, key.lower().replace(' ', '_')] = mapping.get(input_dict.get(key), 0)

    # Age group
    df.at[0, 'age_group'] = encode_age(input_dict.get('Age', 0))

    # One-hot encoding
    for key, values in ONE_HOT_KEYS.items():
        col_name = values.get(input_dict.get(key))
        if col_name in df.columns:
            df.at[0, col_name] = 1

    # Derived features
    freq = df.at[0, 'consume_frequency(weekly)']
    aware = df.at[0, 'awareness_of_other_brands']
    df.at[0, 'cf_ab_score'] = round(freq / (freq + aware), 2) if (freq + aware) > 0 else 0
    df.at[0, 'zas_score'] = df.at[0, 'zone'] * df.at[0, 'income_levels']
    df.at[0, 'bsi'] = int(
        input_dict.get('Current Brand') != 'Established' and
        input_dict.get('Reasons for choosing brands') in ['Price', 'Quality']
    )

    return df

def predict(input_dict):
    input_df = preprocess_input(input_dict)
    pred = model.predict(input_df)[0]
    return PRICE_MAP.get(pred, "Unknown")
