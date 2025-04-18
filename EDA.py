
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

# Load the dataset from uploaded file
df = pd.read_csv(r"C:\Users\anony\Downloads\python.csv", encoding='ISO-8859-1')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ------------------------------------------
# 1. Dataset Overview
# ------------------------------------------
print("📁 Dataset Shape:", df.shape)
print("🧾 Column Names:\n", df.columns.tolist())
print("\n🔍 Data Types:\n", df.dtypes)

# ------------------------------------------
# 2. Numerical Summary for ALL Numerical Columns
# ------------------------------------------
numerical = df.select_dtypes(include=[np.number])

print("\n📊 Numerical Summary (Full):")
print(numerical.describe().T)

# ------------------------------------------
# 3. Advanced Stats: Skewness & Kurtosis
# ------------------------------------------
print("\n📐 Skewness & Kurtosis:")
for col in numerical.columns:
    print(f"\n🔸 {col}")
    print(f"Skewness : {skew(df[col].dropna()):.2f}")
    print(f"Kurtosis : {kurtosis(df[col].dropna()):.2f}")

# ------------------------------------------
# 4. Central Tendency + Range
# ------------------------------------------
print("\n📏 Central Tendency + Spread:")
for col in numerical.columns:
    col_data = df[col].dropna()
    print(f"\n🔹 {col}")
    print(f"Mean      : {col_data.mean():.2f}")
    print(f"Median    : {col_data.median():.2f}")
    print(f"Mode      : {col_data.mode().iloc[0] if not col_data.mode().empty else 'N/A'}")
    print(f"Min       : {col_data.min()}")
    print(f"Max       : {col_data.max()}")
    print(f"Range     : {col_data.max() - col_data.min()}")
    print(f"Std Dev   : {col_data.std():.2f}")
    print(f"IQR       : {col_data.quantile(0.75) - col_data.quantile(0.25):.2f}")
