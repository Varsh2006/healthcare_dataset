#data cleaning

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create a Streamlit app
st.title("Healthcare Dataset Cleaning")
st.write("This app cleans and displays the healthcare dataset.")

# Load the dataset
file_path = 'C:\\Users\\admin\\Desktop\\VARSHA\\Python\\healthcare_dataset.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error("File not found. Please check the file path.")
    st.stop()

# Display the first few rows and information about the dataframe
st.header("Initial DataFrame")
st.write(df.head())
st.write(df.info())

# Handling Missing Values
st.header("Missing Values in Each Column")
st.write(df.isnull().sum())

# Correct Data Types
st.header("Correcting Data Types")
df = df.astype({
    'Name': 'str',  
    'Age': 'int64',
    'Gender': 'str',  
    'Blood Type': 'str',  
    'Medical Condition': 'str',  
    'Date of Admission': 'datetime64[ns]',  
    'Doctor': 'str', 
    'Hospital': 'str',  
    'Insurance Provider': 'str', 
    'Billing Amount': 'float64',
    'Room Number': 'int64',
    'Admission Type': 'str', 
    'Discharge Date': 'datetime64[ns]', 
    'Medication': 'str',  
    'Test Results': 'str' 
})

st.header("Data Types After Correction")
st.write(df.dtypes)

# Display the cleaned DataFrame
st.header("Cleaned DataFrame")
st.dataframe(df)

#file handling


# Function to save cleaned data to a CSV file
def save_cleaned_data(df, file_path='clean_healthcare_dataset.csv'):
    df.to_csv(file_path, index=False)
    st.success(f"Data saved to {file_path}")

# Function to load cleaned data from a CSV file
def load_cleaned_data(file_path='clean_healthcare_dataset.csv'):
    df = pd.read_csv(file_path)
    st.success(f"Data loaded from {file_path}")
    return df

def main():
    st.title('HealthCare Data Analysis')

    # Load initial dataset
    original_file_path = 'healthcare_dataset.csv'  # Adjust the file path as needed
    df = pd.read_csv(original_file_path)

    # Data cleaning steps
    df = df.astype({
    'Name': 'str',  
    'Age': 'int64',
    'Gender': 'str',
    'Blood Type': 'str', 
    'Medical Condition': 'str',  
    'Date of Admission': 'datetime64[ns]', 
    'Doctor': 'str',  
    'Hospital': 'str', 
    'Insurance Provider': 'str',  
    'Billing Amount': 'float64',
    'Room Number': 'int64',
    'Admission Type': 'str',  
    'Discharge Date': 'datetime64[ns]',  
    'Medication': 'str',  
    'Test Results': 'str'  
})    
    # Save cleaned data
    if st.button('Save Cleaned Data'):
        save_cleaned_data(df)

    # Load cleaned data
    if st.button('Load Cleaned Data'):
        cleaned_df = load_cleaned_data()
        st.write(cleaned_df.head())

if __name__ == "__main__":
    main()



#exception handling

try:
    healthcare_data = pd.read_csv(file_path)
    print("File read successfully!")
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except pd.errors.ParserError:
    print("Error: The file could not be parsed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Display the first few rows of the dataset
healthcare_data.head()


#visualization


num = st.selectbox('Select',df.columns,index=14)


st.subheader('Bar Chart')
st.bar_chart(df[num].head(30),color='#BA55D3')

st.subheader('Line Chart')
st.line_chart(df[num].head(30))

st.subheader('Scatter Chart')
st.scatter_chart(df[num].head(30))

st.subheader('Pie Chart')
plt.figure(figsize=[10,10])
plt.pie(df[num].head(30).value_counts().values,labels=df[num].head(30).value_counts().index, colors=['#F6CEFC','white'], autopct='%1.2f%%')
st.pyplot(plt)

st.subheader('Horizontal Bar Chart')
plt.figure(figsize=[10,10])
plt.barh(df[num].head(30).value_counts().values,df[num].head(30).value_counts().index)
st.pyplot(plt)


#dashboard

st.title("Healthcare Data Dashboard")

# Create tabs for each distribution
tabs = ["Age Distribution", "Gender Distribution", "Blood Type Distribution", "Medical Condition Distribution", "Medication Distribution", "Test Results Distribution"]
tab = st.selectbox("Select a distribution:", tabs)

# Define a function to plot the distribution of a column
def plot_distribution(data, column, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    
    if data[column].dtype == 'object':
        data[column].value_counts().plot(kind='bar', color='skyblue')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    else:
        data[column].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    
    plt.title(title)
    st.pyplot(plt)  # Use st.pyplot to display the plot in Streamlit

# Plot distributions based on the selected tab
if tab == "Age Distribution":
    plot_distribution(healthcare_data, 'Age', 'Age Distribution', 'Age', 'Frequency')
elif tab == "Gender Distribution":
    plot_distribution(healthcare_data, 'Gender', 'Gender Distribution', 'Count', 'Gender')
elif tab == "Blood Type Distribution":
    plot_distribution(healthcare_data, 'Blood Type', 'Blood Type Distribution', 'Count', 'Blood Type')
elif tab == "Medical Condition Distribution":
    plot_distribution(healthcare_data, 'Medical Condition', 'Medical Condition Distribution', 'Count', 'Medical Condition')
elif tab == "Medication Distribution":
    plot_distribution(healthcare_data, 'Medication', 'Medication Distribution', 'Count', 'Medication')
elif tab == "Test Results Distribution":
    plot_distribution(healthcare_data, 'Test Results', 'Test Results Distribution', 'Count', 'Test Results')




#analysis

def save_cleaned_data(data):
    # Add your data cleaning logic here
    return data

def main():
    print("Welcome to the Healthcare data analysis!")
    print("Options:")
    print("1. Clean and visualize data")
    print("2. Start Streamlit dashboard")
    print("3. Exit")

    while True:
        option = input("Enter your choice (1/2/3): ")

        if option == "1":
            file_path = input("Enter the file path: ")
            try:
                data = pd.read_csv(file_path)
                cleaned_data = save_cleaned_data(data)
                
                # Perform data visualization
                st.write("Data visualization")
                st.write(cleaned_data.describe())
                
                print("Data visualization completed successfully!")
                
            except (FileNotFoundError,pd.errors.EmptyDataError,pd.errors.ParserError ) as e:
                print(f"Error: {str(e)}")
        
        elif option == "2":
            file_path = input("Enter the file path: ")
            try:
                data = pd.read_csv(file_path)
                st.write("Streamlit dashboard")
                column = st.selectbox('Select a column', data.columns)
                title = f"Distribution of {column}"
                xlabel = "Value"
                ylabel = "Frequency"
                
                if data[column].dtype.kind == 'O':
                    data[column].value_counts().plot(kind='bar', color='skyblue')
                else:
                    data[column].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
                
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                st.pyplot(plt)
                
                print("Streamlit dashboard started successfully!")
                
            except (FileNotFoundError,pd.errors.EmptyDataError,pd.errors.ParserError ) as e:
                print(f"Error: {str(e)}")
        
        elif option == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()













