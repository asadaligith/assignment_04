import streamlit as st

st.markdown("""
    <style>
        body {
            background-color: #f0f8ff; /* Light blue background */
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #2c3e50; /* Dark blue color for title */
            text-align: center;
            font-size: 40px;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
        .bmi-category {
            font-size: 18px;
            text-align: center;
            color: #16a085;
        }
        .warning {
            color: #e74c3c; /* Red color for warning */
            text-align: center;
        }
        .success {
            color: #27ae60; /* Green color for success */
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title BMI Calculator
st.markdown('<div class="title">BMI CALCULATOR</div>', unsafe_allow_html=True)

height = st.slider("Height in CM", 100, 250, 170 )   # define height
weight = st.slider("Weight in KG", 30, 200, 60 )     # define weight

bmi = weight / ((height / 100)**2)                  # BMI formula result

st.success(f"Your BMI is **{bmi:.2f}**")

if bmi < 18.5:                                       # conditions showing to the user about their BMI 
    st.warning("You are underweight.")
elif 18.5 <= bmi < 24.9:
    st.success("You have a normal weight.")
elif 25 <= bmi < 29.9:
    st.warning("You are overweight.")
else:
    st.error("You are obese.")