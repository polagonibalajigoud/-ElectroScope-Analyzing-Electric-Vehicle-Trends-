import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv(r"C:\Users\anony\Downloads\python.csv", encoding='ISO-8859-1')

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w]', '_', regex=True)

# Display cleaned column names
print("Cleaned columns:", df.columns.tolist())

# Handle missing values
df['city'] = df['city'].fillna('Unknown').str.title()
df['state'] = df['state'].fillna('Unknown').str.upper()
df['make'] = df['make'].fillna('Unknown').str.title()
df['model'] = df['model'].fillna('Unknown').str.title()
df['electric_vehicle_type'] = df['electric_vehicle_type'].fillna('Unknown').str.title()
df['clean_alternative_fuel_vehicle__cafv__eligibility'] = df['clean_alternative_fuel_vehicle__cafv__eligibility'].fillna('Unknown')

# Convert numeric columns
numeric_cols = ['electric_range', 'base_msrp', 'model_year']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with invalid model year or range if needed
df = df[(df['model_year'] >= 1990) & (df['model_year'] <= 2025)]

# Strip and title-case locations
df['vehicle_location'] = df['vehicle_location'].fillna('Unknown').str.title()

# Convert categorical columns
categorical_cols = ['make', 'model', 'city', 'state', 'electric_vehicle_type']
for col in categorical_cols:
    df[col] = df[col].astype('category')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Final output
print("\nCleaned EV Data Preview:")
print(df.head())
