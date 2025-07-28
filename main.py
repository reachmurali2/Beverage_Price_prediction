import streamlit as st 
from prediction_helper import predict


st.set_page_config(page_title="Codex Beverage: Price Prediction", layout = "wide")
st.title("Codex Beverage: Price Prediction")

# Create rows of 4 columns each
row1 = st.columns(4) 
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4) 

# Assign inputs to the first row with default values

# ---------------------- Row 1 --------------------------
# row1  0,1,2,3, columns
with row1[0]:                      # Row1 , 0 column
    age = st.number_input('Age', min_value=10, step=1, max_value=100, value=10)
    # st.caption("📌 Available data for age groups: **18–25**, **36–45**, **56–70**")
with row1[1]:
    gender = st.selectbox('Gender', ['M', 'F'])
with row1[2]:
    zone = st.selectbox('Zone', ['rural','semi-urban', 'urban','metro'])  
with row1[3]:
    occupation = st.selectbox('Occupation', ['Working Professional', 'Student', 'Entrepreneur', 'Retired'])

# ---------------------- Row 2 --------------------------
# row2 with 0,1,2,3 columns
with row2[0]:
    income_levels = st.selectbox('Income Level (in L)', ['<10L', '10L - 15L','16 - 25L', '26 - 35L','> 35L'])
with row2[1]:
    consume_frequency= st.selectbox('Consume Frequency(Weekly)', ['0-2 times','3-4 times','5-7 times'])
with row2[2]:
    current_brand = st.selectbox('Current Brand',['Newcomer','Established'])
with row2[3]:
    consumption_size = st.selectbox('Preferable Consumption Size',['Small (250 ml)','Medium (500ml)', 'Large (1L)'])

# ---------------------- Row 3 --------------------------
# row3 with 0,1,2,3 column
with row3[0]:
    brand_awareness = st.selectbox('Awareness of Other Brands', ['0 to 1','2 to 4', 'above 4'])
with row3[1]:
    choosing_brands = st.selectbox('Reasons for choosing brands', ['Price', 'Quality', 'Availability', 'Brand Reputation'])
with row3[2]:
    flavor_preference = st.selectbox('Flavor Preference', ['Traditional', 'Exotic'])
with row3[3]:
    purchase_channel = st.selectbox('Purchase Channel', ['Online', 'Retail Store'])    

# ---------------------- Row 4 --------------------------
# row with 0,1,2 columns 
with row4[0]:
    packaging_preference = st.selectbox('Packaging Preference', ['Simple', 'Premium', 'Eco-Friendly'])
with row4[1]:
    health_concerns = st.selectbox('Health Concerns', ['Low (Not very concerned)', 'Medium (Moderately health-conscious)', 'High (Very health-conscious)'])
with row4[2]:
    typical_consumption_situations = st.selectbox('Typical Consumption Situation', ['Active (eg. Sports, gym)', 'Social (eg. Parties)','Casual (eg. At home)'])


# Create a dictionar for input values
input_dict = {
    'Age': age,                                                        # Age encoding using age_group 
    'Gender': gender,                                                  # Ohe 
    'Zone': zone,                                                      # Label
    'Occupation': occupation,                                          # Ohe 

    'Income Level (in L)':income_levels,                               # Label
    'Consume Frequency(Weekly)':consume_frequency,                     # Label 
    'Current Brand':current_brand,                                     # Ohe
    'Preferable Consumption Size':consumption_size,                    # Label 

    'Awareness of Other Brands': brand_awareness,                      # Label 
    'Reasons for choosing brands':choosing_brands,                     # Ohe 
    'Flavor Preference':flavor_preference,                             # Ohe 
    'Purchase Channel':purchase_channel,                               # Ohe 

    'Packaging Preference':packaging_preference,                       # Ohe 
    'Health Concerns':health_concerns,                                 # Label 
    'Typical Consumption Situation':typical_consumption_situations     # Ohe 
}

# Button to calculate risk: 

# -----------Submit button----------------
st.markdown('###')
if st.button('Calculate Price Range'):
    prediction = predict(input_dict)
    st.success(f"Predicted Price: {prediction}")
    

# ------------------------------ Footer --------------------------------- 

with st.sidebar:
    st.markdown("#### 👤 Murali Krishna")
    st.markdown("AI Engineer | Data Science Enthusiast")

st.markdown("<h4 style='color: gray; text-align: right;'>Developed by <i>Murali Krishna</i></h4>", unsafe_allow_html=True)

st.markdown("""
<hr>
<p style='text-align: center;'>
    <strong>Murali Krishna</strong> | <a href='https://github.com/reachmurali2'>Github</a> | <a href='https://www.linkedin.com/in/murali-krishna-reddy-b-37687979/' target='_blank'>LinkedIn</a> | 
    <a href='mailto:reachmurali2@gmail.com'>Email</a> 
</p>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 15px;'>
    Developed by <strong>Murali Krishna</strong> <br>
    💻 <a href='https://github.com/reachmurali2' target='_blank'>GitHub</a> | &nbsp;
    🔗 <a href='https://www.linkedin.com/in/murali-krishna-reddy-b-37687979/' target='_blank'>LinkedIn</a> &nbsp; | &nbsp;
    📧 <a href='mailto:reachmurali2@gmail.com'>Email</a> &nbsp; 
    
</div>
""", unsafe_allow_html=True)
