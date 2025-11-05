
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# --- Configuration ---
DATA_FILE = "data.csv"
FEATURE_COLUMNS = ['feature1', 'feature2', 'feature3']
TARGET_COLUMN = 'target'
TEST_SIZE = 0.2
RANDOM_STATE = 42

# --- Data Loading and Preprocessing ---
try:
    # Load the dataset
    df = pd.read_csv(DATA_FILE)
    print(f"Successfully loaded '{DATA_FILE}'. Shape: {df.shape}")
except FileNotFoundError:
    print(f"Error: The file '{DATA_FILE}' was not found. Please ensure it is in the correct directory.")
    exit() # Exit if data file is not found
except Exception as e:
    print(f"An error occurred while loading the CSV file: {e}")
    exit()

# Validate if required columns exist
missing_features = [col for col in FEATURE_COLUMNS if col not in df.columns]
if missing_features:
    print(f"Error: Missing feature columns: {', '.join(missing_features)}")
    exit()
if TARGET_COLUMN not in df.columns:
    print(f"Error: Target column '{TARGET_COLUMN}' not found in the dataset.")
    exit()

# Separate features (X) and target (y)
X = df[FEATURE_COLUMNS]
y = df[TARGET_COLUMN]

# --- Handling Missing Values (Imputation) ---
# A common strategy is to impute missing values with the mean of the column.
# This is a basic approach; more sophisticated methods exist.
for col in FEATURE_COLUMNS:
    if X[col].isnull().any():
        mean_val = X[col].mean()
        X[col].fillna(mean_val, inplace=True)
        print(f"Imputed missing values in '{col}' with mean: {mean_val:.2f}")

if y.isnull().any():
    mean_val_y = y.mean()
    y.fillna(mean_val_y, inplace=True)
    print(f"Imputed missing values in target column '{TARGET_COLUMN}' with mean: {mean_val_y:.2f}")

# Ensure there are no remaining NaNs (e.g., if a column was all NaNs)
X = X.dropna(axis=1) # Drop columns that might have become all NaN after imputation attempts if they were empty to start with
y = y.dropna()

# Re-align X and y if any columns were dropped (though unlikely with imputation)
X = X.loc[y.index]

if X.empty or y.empty:
    print("Error: No valid data remaining after preprocessing. Exiting.")
    exit()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

print(f"Data split complete: {len(X_train)} training samples, {len(X_test)} testing samples.")

# --- Model Training ---
# Initialize and train the Linear Regression model
model = LinearRegression()
try:
    model.fit(X_train, y_train)
    print("Linear Regression model trained successfully.")
except Exception as e:
    print(f"An error occurred during model training: {e}")
    exit()

# --- Model Evaluation ---
print("\n--- Model Evaluation ---")

# Make predictions on the test set
try:
    y_pred = model.predict(X_test)
except Exception as e:
    print(f"An error occurred during prediction on test set: {e}")
    exit()

# Evaluate the model using multiple metrics
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse) # RMSE is the square root of MSE

print(f"Model R-squared score: {r2:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")

# --- Making Predictions on New Data ---
print("\n--- New Data Prediction ---")

# Example of making a prediction on new data
# Ensure the new data has the same columns as the training features, in the same order.
# It's good practice to use the same column names as in the training data.
new_data_values = {'feature1': [10], 'feature2': [20], 'feature3': [30]}

# Create a DataFrame for new data, aligning with the original feature columns
# This handles potential reordering or missing columns if X was modified
# We use the columns from X.columns which are the actual features used for training.
new_data = pd.DataFrame(new_data_values)

# Ensure new_data has all the feature columns and in the correct order.
# If a feature was entirely missing from the original X, it won't be in X.columns.
# For simplicity, we assume all FEATURE_COLUMNS are present in new_data_values.
# A more robust solution would involve checking for all features in X.columns and adding
# them with a default or imputed value if missing in new_data_values.

try:
    # Select columns for prediction that match the training data
    new_data_processed = new_data[FEATURE_COLUMNS]
    
    # Handle potential NaNs in new data if necessary (e.g., impute with means from training data)
    for col in FEATURE_COLUMNS:
        if new_data_processed[col].isnull().any():
            # Use the mean from the training data if available
            # In this simplified example, we'll assume new_data has no NaNs for simplicity
            # or imputation logic would need access to training data means.
            print(f"Warning: Missing values found in new data column '{col}'. Prediction might be affected.")
            # Example: new_data_processed[col].fillna(X_train[col].mean(), inplace=True)
            
    prediction = model.predict(new_data_processed)
    print(f"Prediction for new data {new_data_values}: {prediction[0]:.4f}")

except KeyError as e:
    print(f"Error: Missing column in new data for prediction: {e}. Ensure all feature columns are provided.")
except Exception as e:
    print(f"An error occurred during prediction on new data: {e}")
