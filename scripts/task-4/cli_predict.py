import argparse
import pandas as pd
import joblib
import json

# Load models and preprocessor
severity_model = joblib.load("models/severity_model.pkl")
probability_model = joblib.load("models/probability_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# Constants
EXPENSES_MARGIN = 500

# Required features
features = ["RegistrationYear", "TransactionMonth",
            "Province", "Gender", "TotalPremium"]


def preprocess_input(df):
    df = df.copy()
    df["TransactionMonth"] = pd.to_datetime(
        df["TransactionMonth"], errors='coerce', dayfirst=True)
    df["TransactionYear"] = df["TransactionMonth"].dt.year
    df["VehicleAge"] = df["TransactionYear"] - df["RegistrationYear"]
    return df[["VehicleAge", "TotalPremium", "Province", "Gender"]]


def predict(data_path):
    df = pd.read_csv(data_path)
    X_raw = preprocess_input(df)
    X = preprocessor.transform(X_raw)

    # Predictions
    p_claim = probability_model.predict_proba(X)[:, 1]
    claim_amount = severity_model.predict(X)
    premium = (p_claim * claim_amount) + EXPENSES_MARGIN

    # Output results
    df_result = df.copy()
    df_result["Predicted_Claim_Prob"] = p_claim
    df_result["Predicted_Severity"] = claim_amount
    df_result["Predicted_Premium"] = premium

    print(df_result[["Predicted_Claim_Prob", "Predicted_Severity",
          "Predicted_Premium"]].to_json(orient="records", lines=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI for Risk-Based Premium Prediction")
    parser.add_argument("--data", type=str, help="Path to input CSV data")
    args = parser.parse_args()
    predict(args.data)
