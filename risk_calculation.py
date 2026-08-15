import pandas as pd

def calculate_risk_score(df):
    # Calculate a simple risk score based on severity
    # Weightings: Death=10, Injury=3, Accident=1
    
    df['Risk_Score'] = (df['Number_of_Deaths'] * 10) + \
                       (df['Number_of_Injuries'] * 3) + \
                       (df['Number_of_Accidents'] * 1)
                       
    # Normalize risk score between 0 and 1
    max_score = df['Risk_Score'].max()
    df['Normalized_Risk'] = df['Risk_Score'] / max_score
    
    return df

if __name__ == "__main__":
    print("Risk calculation module ready.")
    