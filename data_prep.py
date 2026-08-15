import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    # This simulates loading data from Sri Lanka Open Data Portal
    # Replace with actual pd.read_csv(filepath) when you have the dataset
    
    data = {
        'District': ['Colombo', 'Gampaha', 'Kandy', 'Galle', 'Kurunegala'],
        'Road_Name': ['A1', 'A3', 'A2', 'A4', 'A6'],
        'Number_of_Accidents': [150, 120, 80, 90, 110],
        'Number_of_Deaths': [15, 10, 5, 8, 12],
        'Number_of_Injuries': [50, 40, 20, 30, 45],
        'Latitude': [6.9271, 7.0873, 7.2906, 6.0535, 7.4818],
        'Longitude': [79.8612, 79.9992, 80.6337, 80.2210, 80.3609]
    }
    
    df = pd.DataFrame(data)
    
    # Pre-processing: Fill missing values
    df.fillna(0, inplace=True)
    return df

if __name__ == "__main__":
    df = load_and_clean_data("dummy_path.csv")
    print("Data pre-processing complete. Sample data:")
    print(df.head())