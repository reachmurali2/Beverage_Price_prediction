# 🧃 Codex Beverage: Price Prediction App

This Streamlit web app predicts the **preferred price range** (in ₹) for a new beverage product based on consumer demographic and behavioral inputs. It uses a machine learning classification model trained on customer survey data to segment users into one of four price brackets.

---

## 🚀 Features

- Clean, responsive UI using **Streamlit**
- Accepts user inputs like:
  - Age, Gender, Zone, Occupation
  - Income level, Consumption habits
  - Brand preferences and awareness
  - Health concerns, flavor and packaging choices
- Predicts one of four price ranges:
  - ₹50–100, ₹100–150, ₹150–200, ₹200–250
- Includes engineered features:
  - **CF/AB Score**: Consumption Frequency vs. Brand Awareness
  - **ZAS Score**: Zone × Affluence
  - **BSI (Brand Switch Index)**: Captures likelihood of switching from established brands

---

## 🧠 Model

- Pretrained ML model loaded using `pickle`
- Preprocessing includes label encoding, one-hot encoding, and feature engineering
- Prediction logic modularized in `prediction_helper.py`

---

## 📂 File Structure

```
📁 artifacts/
    └── model.pkl                 ← Pretrained model file
📄 main.py                        ← Streamlit frontend
📄 prediction_helper.py          ← Input preprocessing and prediction logic
```

---

## 🛠 How to Run

```bash
pip install -r requirements.txt
streamlit run main.py
```

---

## 👨‍💻 Developed by

**Murali Krishna**  
[GitHub](https://github.com/reachmurali2) • [LinkedIn](https://www.linkedin.com/in/murali-krishna-reddy-b-37687979/) • [Email](mailto:reachmurali2@gmail.com)