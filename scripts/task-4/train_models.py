import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("data/MachineLearningRating_v3.csv", low_memory=False)

# Drop rows with missing core values
df = df.dropna(subset=["TotalClaims", "TotalPremium",
               "RegistrationYear", "Province", "Gender"])

# Feature Engineering: Estimate Vehicle Age
df["TransactionYear"] = df["TransactionMonth"].str[:4].astype(int)
df["VehicleAge"] = df["TransactionYear"] - df["RegistrationYear"]

# Binary target for claim classification
df["HasClaim"] = (df["TotalClaims"] > 0).astype(int)
df_claims = df[df["TotalClaims"] > 0].copy()

# Final features
features = ["VehicleAge", "TotalPremium", "Province", "Gender"]
num_cols = ["VehicleAge", "TotalPremium"]
cat_cols = ["Province", "Gender"]

# Targets
target_prob = df["HasClaim"]
target_sev = df_claims["TotalClaims"]

# Preprocessor
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
])

# Fit on combined data
X_all = pd.concat([df[features], df_claims[features]]).drop_duplicates()
preprocessor.fit(X_all)

# Save preprocessor
Path("models").mkdir(exist_ok=True)
joblib.dump(preprocessor, "models/preprocessor.pkl")

# Fit classification model
X_prob = preprocessor.transform(df[features])
clf = LogisticRegression(max_iter=1000)
clf.fit(X_prob, target_prob)
joblib.dump(clf, "models/probability_model.pkl")

# Fit severity model
X_sev = preprocessor.transform(df_claims[features])
reg = RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X_sev, target_sev)
joblib.dump(reg, "models/severity_model.pkl")

print("✅ Models and preprocessor saved to /models")
