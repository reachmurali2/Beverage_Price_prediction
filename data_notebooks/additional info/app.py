import streamlit as st

st.set_page_config(page_title="CodeX Beverage: Price Prediction", layout="wide")

st.title("CodeX Beverage: Price Prediction")

# Create a 3-column layout for form inputs
col1, col2, col3 = st.columns(3)

# ----------- First Row -----------
with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=28, step=1)
    st.caption("📌 Available data age groups: **18–25**, **36–45**, **56–70**")

with col2:
    gender = st.selectbox("Gender", ["M", "F", "Other"])

with col3:
    zone = st.selectbox("Zone", ["Urban", "Semi-Urban", "Rural"])

# ----------- Second Row -----------
col4, col5, col6 = st.columns(3)

with col4:
    income_level = st.selectbox("Income Level (In L)", ["<10L", "10L-25L", "25L-50L", "50L+"])

with col5:
    frequency = st.selectbox("Consume Frequency (weekly)", ["0-2 times", "3-5 times", "6+ times"])

with col6:
    occupation = st.selectbox("Occupation", ["Student", "Working Professional", "Business Owner", "Retired"])

# ----------- Third Row -----------
col7, col8, col9 = st.columns(3)

with col7:
    current_brand = st.selectbox("Current Brand", ["Newcomer", "Established", "Premium"])

with col8:
    consumption_size = st.selectbox("Preferable Consumption Size", ["Small (250 ml)", "Medium (500 ml)", "Large (1L)"])

with col9:
    purchase_channel = st.selectbox("Purchase Channel", ["Online", "Offline", "Both"])

# ----------- Fourth Row -----------
col10, col11, col12 = st.columns(3)

with col10:
    brand_awareness = st.selectbox("Awareness of other brands", ["0 to 1", "2 to 3", "4+"])

with col11:
    reason = st.selectbox("Reasons for choosing brands", ["Price", "Taste", "Availability", "Brand Reputation"])

with col12:
    flavor_pref = st.selectbox("Flavor Preference", ["Traditional", "Fruity", "Spicy", "Herbal"])

# ----------- Fifth Row -----------
col13, col14, col15 = st.columns(3)

with col13:
    packaging = st.selectbox("Packaging Preference", ["Simple", "Premium", "Eco-friendly"])

with col14:
    health_concerns = st.selectbox("Health Concerns", ["Low (Not very concerned)", "Moderate", "High"])

with col15:
    situation = st.selectbox("Typical Consumption Situations", [
        "Active (eg. Sports, gym)", 
        "Work/Study", 
        "Leisure (movies, relaxing)", 
        "With friends/family"
    ])

# ----------- Button -----------
st.markdown("###")
if st.button("Calculate Price Range"):
    # You can replace this with actual ML logic later
    st.success("📈 Predicted price range: ₹35 – ₹45 per 250ml unit")
