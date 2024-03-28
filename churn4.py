import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image
import base64  # Import base64 module for encoding data for download

# Load the model
def load_model():
    try:
        with open('churn_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

model = load_model()

# Function for making predictions
def churn_prediction(input_df):
    prediction = model.predict(input_df)
    return prediction


# Function for calculating churn risk levels
def calculate_churn_risk(input_df):
    y_probabilities = model.predict_proba(input_df)
    churn_probabilities = y_probabilities[:, 1]

    # Define thresholds for risk levels
    threshold_high = 0.6
    threshold_medium = 0.4

    # Categorize customers based on predicted probabilities
    churn_risk_levels = np.where(churn_probabilities >= threshold_high, 'High Risk',
                                 np.where(churn_probabilities >= threshold_medium, 'Medium Risk', 'Low Risk'))

    # Return the churn risk levels
    return churn_risk_levels

# Streamlit UI
def main():
    st.set_page_config(page_title='Customer churn prediction', layout='wide')
    
    # Add image
    image = Image.open('customer_service_2.png')
    st.image(image, use_column_width=False)
    
    # Add title
    st.title('Customer Churn Risk Prediction')
 
    # Option to upload CSV file
    st.write('### Upload CSV File')
    # Information about the expected CSV file format
    st.write('**Header Row**: The first row of the CSV file should contain column headers, each representing a specific attribute or variable.')
    st.write('- `MonthlyMinutes` (float): How many minutes does the customer use per month?')
    st.write('- `TotalRecurringCharge` (float): What is the amount of fixed charges?')
    st.write('- `PercChangeMinutes` (float, can be negative): How has the minutes usage changed over the given time period?')
    st.write('- `UniqueSubs` (int): How many unique subscriptions does the customer have?')
    st.write('- `Handsets` (int): How many handsets does the customer own?')
    st.write('- `CurrentEquipmentDays` (int): How many days is the customer\'s equipment old?')
    st.write('- `HandsetRefurbished` (1/0): Is the customer using a refurbished handset?')
    st.write('- `HandsetWebCapable` (1/0): Is the handset web capable?')
    st.write('- `RetentionCalls` (int): How many retention calls were made?')
    st.write('- `RetentionOffersAccepted` (1 or 0): Was the retention offer accepted?')
    st.write('- `CreditRating` (1 to 7): The credit rating of the customer.')
    st.write('**Data Rows**: Following the header row, each subsequent row should contain data entries. Each entry should align with the corresponding column headers, adhering to the specified data format and content requirements.')
    st.write('**Data Format**: Data entries should be in a standardized format consistent with the data type of the corresponding column. For example, numerical values should be formatted as numbers, dates should follow a specific date format, and text entries should be appropriately encoded.')
    st.write('**Content Correspondence**: The content of the CSV file must accurately reflect the information being represented. Each data entry should provide relevant and valid information corresponding to the column it belongs to.')
    
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    # If file is uploaded, display data, make predictions, and allow downloading
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Drop the 'Unnamed: 0' column if it exists
            if 'Unnamed: 0' in df.columns:
                df.drop('Unnamed: 0', axis=1, inplace=True)
            
            # Convert any remaining object columns to numeric, if possible
            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except ValueError:
                        pass  # Skip columns that cannot be converted
                    
            # Ensure all columns have numeric data types
            df = df.astype(float)
            
            prediction = churn_prediction(df)
            churn_risk_levels = calculate_churn_risk(df)
            
            df['Prediction'] = prediction
            df['Churn Risk Level'] = churn_risk_levels
            st.write(df)
            
            # Add a download button to download the prediction results
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Convert DataFrame to base64
            href = f'<a href="data:file/csv;base64,{b64}" download="predictions.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error processing CSV file: {e}")

# Run the app
if __name__ == '__main__':
    main()