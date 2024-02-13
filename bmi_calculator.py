import streamlit as st

def main():
    st.title("BMI Calculator")

    weight = st.number_input("Enter your weight (in kg)")
    height = st.number_input("Enter your height (in cm)")

    if st.button("Calculate BMI"):
        height /= 100  # Convert height to meters
        bmi = weight / (height * height)
        st.write("Your BMI is:", bmi)

if __name__ == "__main__":
    main()