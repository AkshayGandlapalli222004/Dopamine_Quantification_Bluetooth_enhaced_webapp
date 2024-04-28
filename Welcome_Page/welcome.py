import streamlit as st
import os

def main():
    # Header
    st.title("Dopamine Dashboard")

    # Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Data Preview", "Data Preparation", "Smoothing and Filtering", "Classification", "Regression"])

    # Handle navigation
    if page == "Home":
        show_home_page()
    elif page == "About":
        show_about_page()
    elif page == "Data Preview":
        show_data_preview_page()
    elif page == "Data Preparation":
        show_data_preparation_page()
    elif page == "Smoothing and Filtering":
        show_smoothing_filtering_page()
    elif page == "Classification":
        show_classification_page()
    elif page == "Regression":
        show_regression_page()

def show_home_page():
    st.write("Welcome to the home page! This page serves as the starting point of your journey through the Dopamine Quantification Dashboard. From here, you can navigate to different sections of the dashboard using the sidebar on the left.")

def show_about_page():
    st.write("About the Dopamine Dashboard")
    st.write("The Dopamine Dashboard is a data analysis tool developed by Sai Akshay Gandlapalli Team. It allows users to analyze data from a Bluetooth-enhanced biosensor to quantify dopamine levels. This dashboard offers various features to explore and analyze the data effectively.")
    st.write("The development team behind this dashboard consists of passionate individuals dedicated to providing a user-friendly interface for data analysis. We aim to empower researchers and professionals in the field of neuroscience by providing them with powerful tools to analyze dopamine-related data.")

def show_data_preview_page():
    st.write("Data Preview Page")
    st.write("On the Data Preview page, you can have a general look at your dataset and spot some correlations between the features. This helps in understanding the structure of the data and identifying initial patterns.")
    st.write("You can visualize different aspects of the dataset such as summary statistics, distribution plots, and correlation matrices. This exploration step is crucial for gaining insights into the data before performing further analysis.")

def show_data_preparation_page():
    st.write("Data Preparation Page")
    st.write("The Data Preparation page allows you to prepare your data for analysis. You can drop or rename single/multiple columns, and make necessary changes to ensure the data is ready for further processing.")
    st.write("Data preparation tasks may include handling missing values, encoding categorical variables, and scaling numerical features. By cleaning and transforming the data appropriately, you can improve the accuracy and reliability of your analysis results.")

def show_smoothing_filtering_page():
    st.write("Smoothing and Filtering Page")
    st.write("In the Smoothing and Filtering page, you can use a multitude of tools to trim or adjust your data to increase its quality. This includes techniques like smoothing, filtering, and interpolation to refine the data.")
    st.write("You can apply various signal processing methods to remove noise from the data and extract meaningful information. These preprocessing steps are essential for improving the accuracy of subsequent analyses, such as classification and regression.")

def show_classification_page():
    st.write("Classification Page")
    st.write("On the Classification page, you can perform several classification methods such as Random Forest and get results as visualization and datasheet. This helps in categorizing data points into different classes based on their features.")
    st.write("Classification algorithms such as decision trees, support vector machines, and k-nearest neighbors can be applied to classify data into predefined categories. You can evaluate the performance of each model and choose the best one for your dataset.")

def show_regression_page():
    st.write("Regression Page")
    st.write("The Regression page allows you to predict the next data points using algorithms like Neural Networks, Random Forest, and others. This is useful for forecasting future trends and making informed decisions based on the data.")
    st.write("Regression analysis helps in modeling the relationship between independent variables and a dependent variable. You can assess the strength of the relationship and make predictions about future outcomes. Techniques like linear regression, polynomial regression, and time series analysis can be applied.")


# Header
st.title("Dopamine Quantification Dashboard with Bluetooth Enhanced Biosensor")

# Description
st.write("""
         Welcome to the Dopamine Quantification Dashboard! This app allows you to analyze data from a Bluetooth-enhanced biosensor to quantify dopamine levels. Developed by Sai Akshay Gandlapalli Team, this dashboard offers various features to explore and analyze your data effectively.
         """)

# Navigation
st.header("Navigation")
st.markdown("""
            - **Welcome:** This is where you currently are
            - **Data Preview:**  You can have a look at your dataset in general and spot some correlations between the features
            - **Data Preparation:** Drop and/or rename single/multiple columns, don't forget to submit changes
            - **Smoothing and Filtering:** Use a multitude of tools to trim or adjust your data to increase its quality. Don't forget to save and finalize the results! Even if you didn't change anything :)
            - **Classification:** You can perform several classification methods (e.g. Random Forest) and get results as visualization and datasheet.  
            - **Regression:** Predict the next data points using Neural Networks, Random Forest and other algorithms
            """)

# Info
st.info("For the best experience, navigate through the pages sequentially!")

# File cleanup from previous runs
if os.path.isfile("Smoothing_and_Filtering//Preprocessing dataset.csv"):
    os.remove("Smoothing_and_Filtering//Preprocessing dataset.csv")
        
if os.path.isfile("Smoothing_and_Filtering//Filtered Dataset.csv"):
    os.remove("Smoothing_and_Filtering//Filtered Dataset.csv")

if os.path.isfile("Smoothing_and_Filtering//initial.csv"):
    os.remove("Smoothing_and_Filtering//initial.csv")
