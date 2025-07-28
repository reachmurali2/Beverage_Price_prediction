
import joblib 
import pickle
import numpy as np 
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# Path to the saved model and its components 
# MODEL_PATH = 'artifacts/model_data.joblib'

# # Load the model and its components
# model_data = joblib.load(MODEL_PATH)
# model = model_data['model']
# # features = model_data['X_train.columns'] 

# @st.cache_resources:                                                              # Streamlit’s @st.cache_resource decorator to cache the machine learning model loaded from a pickle file/joblib file. # Caches the loaded model object so it's not reloaded every rerun, speeding up Streamlit apps.                                                              
#     with open("artifacts/model_data.joblib", "rb")  as f:                         # If plain model is saved in pickle format                     
#         return joblib.load(f)
#           model = load_model()


# Load the model
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)


def preprocess_input(input_dict):

    expected_columns = [
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

    # Manually assign values for each categorical input based on input_dict
    for key, value in input_dict.items():
        if key == 'Zone':
            if value == 'Rural':
                df['zone'] = 1
            elif value == 'Semi-Urban':
                df['zone'] = 2
            elif value == 'Urban':
                df['zone'] = 3
            elif value == 'Metro':
                df['zone'] = 4
        elif key == 'Income Level':
            if value == '<10L':
                df['income_levels'] = 1
            elif value == '10L - 15L':
                df['income_levels'] = 2
            elif value == '16L - 25L':
                df['income_levels'] = 3
            elif value == '26L - 35L':
                df['income_levels'] = 4
            elif value == '> 35L':
                df['income_levels'] = 5
            elif value == 'Not Reported':
                df['income_levels'] = 0
        elif key == 'Consume Frequency(Weekly)':
            if value == '0-2 times':
                df['consume_frequency(weekly)']  = 1
            elif value == '3-4 times':
                df['consume_frequency(weekly)']  = 2
            elif value == '5-7 times':
                df['consume_frequency(weekly)']  = 3
        elif key == 'Preferable Consumption Size':
            if value == 'Small (250 ml)':
                df['preferable_consumption_size'] = 1
            elif value == 'Medium (500 ml)':
                df['preferable_consumption_size'] = 2
            elif value == 'Large (1 L)':
                df['preferable_consumption_size'] = 3
        elif key == 'Awareness of other brands':
            if value == '0 to 1':
                df['awareness_of_other_brands'] = 1
            elif value == '2 to 4':
                df['awareness_of_other_brands'] = 2
            elif value == 'above 4':
                df['awareness_of_other_brands'] = 3
        elif key == 'Health Concerns':
            if value == 'Low (Not very concerned)':
                df['health_concerns'] = 1
            elif value == 'Medium (Moderately health-conscious)':
                df['health_concerns'] = 2
            elif value == 'High (Very health-conscious)':
                df['health_concerns'] = 3
        elif key == 'Age':
            if 18 <= value <= 25:
                df['age_group'] = 1
            elif 26 <= value <= 35:
                df['age_group'] = 2
            elif 36 <= value <= 45:
                df['age_group'] = 3
            elif 46 <= value <= 55:
                df['age_group'] = 4
            elif 56 <= value <= 70:
                df['age_group'] = 5
            else:
                df['age_group'] = 0
        elif key == 'Gender' and value == 'M':
            df['gender_M'] = 1
        elif key == 'Occupation':
            if value == 'Retired':
                df['occupation_Retired'] = 1
            elif value == 'Student':
                df['occupation_Student'] = 1
            elif value == 'Working Professional':
                df['occupation_Working Professional'] = 1
        elif key == 'Current Brand':
            if value == 'Newcomer':
                df['current_brand_Newcomer'] = 1
        elif key == 'Reasons for choosing brands':
            if value == 'Brand Reputation':
                df['reasons_for_choosing_brands_Brand Reputation'] = 1
            elif value == 'Price':
                df['reasons_for_choosing_brands_Price'] = 1
            elif value == 'Quality':
                df['reasons_for_choosing_brands_Quality'] = 1
        elif key == 'Flavor Preference':
            if value == 'Traditional':
                df['flavor_preference_Traditional'] = 1
        elif key == 'Purchase Channel':
            if value == 'Retail Store':
                df['purchase_channel_Retail Store'] = 1
        elif key == 'Packaging Preference':
            if value == 'Premium':
                df['packaging_preference_Premium'] = 1
            elif value == 'Simple':
                df['packaging_preference_Simple'] = 1
        elif key == 'Typical Consumption Situations':
            if value == 'Casual (eg. At home)':
                df['typical_consumption_situations_Casual (eg. At home)'] = 1
            elif value == 'Social (eg. Parties)':
                df['typical_consumption_situations_Social (eg. Parties)'] = 1


    df['cf_ab_score'] = round(df['consume_frequency(weekly)'] / (df['consume_frequency(weekly)'] + df['awareness_of_other_brands']), 2)
    df['zas_score'] = df['zone'] * df['income_levels']
    df['bsi'] = 1 if (input_dict['Current Brand'] != 'Established' and (input_dict['Reasons for choosing brands'] in ['Price', 'Quality'])) else 0

    return df



def predict(input_dict):
    input_df = preprocess_input(input_dict)
    prediction = model.predict(input_df)

    if prediction == 0:
        return '50-100'
    elif prediction == 1:
        return '100-150'
    elif prediction == 2:
        return '150-200'
    elif prediction == 3:
        return '200-250'
