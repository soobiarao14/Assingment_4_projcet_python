

import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 16.0:
        return "Severely underweight (Below 16.0)"
    elif 16.0 <= bmi < 18.5:
        return "Underweight (16.0 - 18.4)"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight (18.5 - 24.9)"
    elif 25.0 <= bmi < 29.9:
        return "Overweight (25.0 - 29.9)"
    elif 30.0 <= bmi < 34.9:
        return "Obese (Class 1) (30.0 - 34.9)"
    elif 35.0 <= bmi < 39.9:
        return "Obese (Class 2) (35.0 - 39.9)"
    else:
        return "Obese (Class 3 - Severe Obesity) (40.0 and above)"

def main():
    st.title("BMI Calculator")
    st.write("Enter your details below to calculate your BMI")
    
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.1, format="%.2f")
    
    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            st.success(f"Your BMI is: {bmi:.2f}")
            st.info(f"Category: {category}")
        else:
            st.error("Height must be greater than zero.")

if __name__ == "__main__":
    main()