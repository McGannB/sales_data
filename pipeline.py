import pandas as pd
import sqlite3


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


#Load Data into a SQL Database


#Load data into SQLite database
def load_data_to_db(data, db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data loaded into {table_name} table in {db_name} database.")
    except Exception as e:
        print(f"Error loading data to database: {e}")

#Load the transformed data
db_name = 'sales_data.db'
table_name = 'sales'
load_data_to_db(transformed_data, db_name, table_name)