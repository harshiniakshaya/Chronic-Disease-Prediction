import pandas as pd
import numpy as np
import os

NUM_SAMPLES = 2000

data = {
    'age': np.random.randint(20, 81, size=NUM_SAMPLES),
    'bmi': np.random.uniform(18.0, 40.0, size=NUM_SAMPLES),
    'servings_veg_fruit_daily': np.random.randint(0, 6, size=NUM_SAMPLES),
    'servings_processed_food_weekly': np.random.randint(0, 21, size=NUM_SAMPLES),
    'hours_exercise_weekly': np.random.randint(0, 15, size=NUM_SAMPLES),
    'hours_sleep_daily': np.random.uniform(4.0, 10.0, size=NUM_SAMPLES),
    'alcohol_units_weekly': np.random.randint(0, 40, size=NUM_SAMPLES),
    'is_smoker': np.random.choice([0, 1], size=NUM_SAMPLES, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# --- Define Rules to Determine Disease Risk ---
# Heart Disease Risk Factors
heart_score = (
    (df['bmi'] > 30) * 1.5 +
    (df['age'] / 10) +
    (df['servings_processed_food_weekly'] > 10) * 1.5 +
    (df['hours_exercise_weekly'] < 2) * 1.0 +
    df['is_smoker'] * 2.0
)

# Liver Disease Risk Factors
liver_score = (
    (df['alcohol_units_weekly'] > 14) * 2.5 +
    (df['bmi'] > 30) * 1.5 +
    (df['servings_processed_food_weekly'] > 7) * 1.0
)

# Kidney Disease Risk Factors
kidney_score = (
    (df['bmi'] > 30) * 1.5 +
    (df['servings_processed_food_weekly'] > 10) * 1.0 +
    (df['age'] / 20) +
    (df['hours_exercise_weekly'] < 3) * 1.0 +
     df['is_smoker'] * 1.5
)

# Add some random noise to make it less predictable
heart_score += np.random.normal(0, 1, size=NUM_SAMPLES)
liver_score += np.random.normal(0, 1, size=NUM_SAMPLES)
kidney_score += np.random.normal(0, 1, size=NUM_SAMPLES)

df['heart_disease_risk'] = (heart_score > np.percentile(heart_score, 75)).astype(int)
df['liver_disease_risk'] = (liver_score > np.percentile(liver_score, 75)).astype(int)
df['kidney_disease_risk'] = (kidney_score > np.percentile(kidney_score, 75)).astype(int)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(BASE_DIR, "lifestyle_data.csv")
df.to_csv(output_path, index=False)

print(f"Successfully generated synthetic dataset with {NUM_SAMPLES} samples.")
print(f"Saved to: {output_path}")
print("\n--- Dataset Preview ---")
print(df.head())
print("\n--- Risk Distribution ---")
print(df[['heart_disease_risk', 'liver_disease_risk', 'kidney_disease_risk']].sum())
