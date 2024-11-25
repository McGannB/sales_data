import pandas as pd

#Extract Data

#Load CSV data
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data extracted successfully.")
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
    
#Example Usage
file_path = 'sales_data.csv' #Replace with the path to your CSV
data = extract_data(file_path)
print(data.head())

#Transform Data

#Clean and process the data
def transform_data(data):
    try:
        #Drop rows with missing values
        data = data.dropna()

        #Convert 'Date' column to datetime format
        data['Date'] = pd.to_datetime(data['Date'])

        #Ensure 'Sales' column is numeric
        data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')
        data = data.dropna(subset=['Sales']) #Drop rows with invalid sales data

        print("Data transformed successfully.")
        return data
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

#Transform the extracted data
transformed_data = transform_data(data)
print(transformed_data.head())


