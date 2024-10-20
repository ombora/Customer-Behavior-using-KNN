# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'random_forest_model.pkl'  # Replace with your model file path
loaded_model = pickle.load(open(filename, 'rb'))

# Define the Streamlit app
def main():
    st.title("Customer Purchase Prediction App")

    # Create input fields for user data
    age = st.number_input("Enter Age:", min_value=18, max_value=100, value=25)
    salary = st.number_input("Enter Salary:", min_value=0, value=50000)
    experience = st.number_input("Enter Experience:", min_value=0, value=5)

    # Select options for education level and city
    education_level = st.selectbox("Education Level", ["High School", "Masters", "PhD"], index=1)
    city = st.selectbox("City", ["Los Angeles", "New York", "San Francisco"], index=1)

    # Create a button to predict
    if st.button("Predict"):
        # Prepare the input data in the exact order used in model training
        input_data = pd.DataFrame({
            "Age": [age],
            "Salary": [salary],
            "Experience": [experience],
            "Education Level_High School": [1 if education_level == "High School" else 0],
            "Education Level_Masters": [1 if education_level == "Masters" else 0],
            "Education Level_PhD": [1 if education_level == "PhD" else 0],
            "City_Los Angeles": [1 if city == "Los Angeles" else 0],
            "City_New York": [1 if city == "New York" else 0],
            "City_San Francisco": [1 if city == "San Francisco" else 0]
        })

        # Reorder the input data to match the training order
        input_data = input_data[[
            "Age", 
            "Salary", 
            "Experience", 
            "Education Level_High School", 
            "Education Level_Masters", 
            "Education Level_PhD", 
            "City_Los Angeles", 
            "City_New York", 
            "City_San Francisco"
        ]]

        # Make a prediction using the loaded model
        prediction = loaded_model.predict(input_data)

        # Display the prediction (target: Buys Expensive Product)
        if prediction[0] == 1:
            st.success("The customer is likely to buy expensive products.")
        else:
            st.warning("The customer is likely not to buy expensive products.")

if __name__ == "__main__":
    main()
