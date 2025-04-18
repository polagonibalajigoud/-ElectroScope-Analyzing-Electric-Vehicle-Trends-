import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, ttest_1samp
import scipy.stats as stats

# Step 1: Load the dataset
df = pd.read_csv(r"C:\Users\anony\Downloads\python.csv")  # Adjust path if needed

# Step 2: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# -----------------------------
# Independent Two-Sample T-Test
# -----------------------------
bev = df[(df['electric_vehicle_type'] == 'Battery Electric Vehicle (BEV)') & (df['base_msrp'].notnull())]['base_msrp']
phev = df[(df['electric_vehicle_type'] == 'Plug-in Hybrid Electric Vehicle (PHEV)') & (df['base_msrp'].notnull())]['base_msrp']

t_stat, p_value = ttest_ind(bev, phev, equal_var=False)  # Welch’s t-test

print("Independent Two-Sample T-Test")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: Vehicle prices are significantly different between BEV and PHEV.")
else:
    print("Fail to reject the null hypothesis: No significant difference in vehicle prices.")

# -----------------------------
# One Sample T-Test
# -----------------------------
electric_range = df['electric_range'].dropna()

t_stat, p_value = ttest_1samp(electric_range, 150)  # Test if mean differs from 150

print("\nOne Sample T-Test")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: The average electric range is significantly different from 150 miles.")
else:
    print("Fail to reject the null hypothesis: No significant difference from 150 miles.")

# -----------------------------
# Chi-Square Test
# -----------------------------
chi_df = df.dropna(subset=['electric_vehicle_type', 'clean_alternative_fuel_vehicle_(cafv)_eligibility'])

contingency_table = pd.crosstab(chi_df['electric_vehicle_type'], chi_df['clean_alternative_fuel_vehicle_(cafv)_eligibility'])

chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print("\nChi-Square Test")
print(f"Chi2 = {chi2:.2f}")
print(f"p-Value = {p:.4f}")

if p < alpha:
    print("Reject the null hypothesis: Significant association between vehicle type and CAFV eligibility.")
else:
    print("Fail to reject the null hypothesis: No significant association found.")
