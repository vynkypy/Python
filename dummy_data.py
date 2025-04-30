import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate Chemistry Table


def generate_chemistry_data(n):
    data = {
        "Compound_ID": [f"CMPD_{i}" for i in range(1, n + 1)],
        "Molecular_Weight": [round(random.uniform(200, 800), 2) for _ in range(n)],
        "Purity (%)": [random.choice([round(random.uniform(85, 99), 2), None]) for _ in range(n)],
        "LogP": [round(random.uniform(-3, 5), 2) for _ in range(n)],
        "Synthesis_Batch": [random.choice(["Batch_1", "Batch_2", "Batch_3", "Batch_4"]) for _ in range(n)],
    }
    return pd.DataFrame(data)

# Generate Formulation Table


def generate_formulation_data(n):
    data = {
        "Formulation_ID": [f"FORM_{i}" for i in range(1, n + 1)],
        "Compound_ID": [f"CMPD_{random.randint(1, n // 2)}" for _ in range(n)],
        "Dosage_Form": [random.choice(["Tablet", "Capsule", "Solution", "Suspension"]) for _ in range(n)],
        "Batch_Size (mg)": [round(random.uniform(100, 1000), 2) for _ in range(n)],
        "Stability (Months)": [random.choice([random.randint(6, 36), None]) for _ in range(n)],
    }
    return pd.DataFrame(data)

# Generate Preclinical Table


def generate_preclinical_data(n):
    data = {
        "Study_ID": [f"STUDY_{i}" for i in range(1, n + 1)],
        "Formulation_ID": [f"FORM_{random.randint(1, n // 2)}" for _ in range(n)],
        "Animal_Type": [random.choice(["Mouse", "Rat", "Dog", "Monkey"]) for _ in range(n)],
        "Dose (mg/kg)": [round(random.uniform(1, 50), 2) for _ in range(n)],
        "Toxicity_Level": [random.choice(["Low", "Medium", "High"]) for _ in range(n)],
        "Observation_Period (Days)": [random.randint(7, 90) for _ in range(n)],
    }
    return pd.DataFrame(data)


# Generate DataFrames
chemistry_data = generate_chemistry_data(100)
formulation_data = generate_formulation_data(100)
preclinical_data = generate_preclinical_data(100)

# Introduce Duplicates and Nulls for Cleaning
chemistry_data.loc[5, "Purity (%)"] = None  # Null value
chemistry_data = pd.concat(
    [chemistry_data, chemistry_data.iloc[:5]])  # Duplicate rows

formulation_data.loc[3, "Dosage_Form"] = None  # Null value
formulation_data = pd.concat(
    [formulation_data, formulation_data.iloc[:10]])  # Duplicate rows

preclinical_data.loc[7, "Toxicity_Level"] = None  # Null value
preclinical_data = pd.concat(
    [preclinical_data, preclinical_data.iloc[:3]])  # Duplicate rows

# Save to CSVs (optional)
chemistry_data.to_csv("chemistry_data.csv", index=False)
formulation_data.to_csv("formulation_data.csv", index=False)
preclinical_data.to_csv("preclinical_data.csv", index=False)

# Display the data
print("Chemistry Data:")
print(chemistry_data.head())
print("\nFormulation Data:")
print(formulation_data.head())
print("\nPreclinical Data:")
print(preclinical_data.head())
