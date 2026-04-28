import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\Documents\Visual Studio 18\Customer_shipping_behaviour\Python file\Data\Raw\customer_shopping_behavior.csv")

print("Original Shape:", df.shape)
print(df.head())
print(df.info())

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("/", "_", regex=False)
)

print("\nUpdated Columns:")
print(df.columns.tolist())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna("Unknown")

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Convert Yes/No type columns to standard format
yes_no_cols = ['Subscription_Status', 'Discount_Applied', 'Promo_Code_Used']
for col in yes_no_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

# Clean text columns
text_cols = ['Gender', 'Category', 'Season', 'Shipping_Type', 'Payment_Method', 'Frequency_of_Purchases']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

# Clean numeric values
if 'Purchase_Amount_USD' in df.columns:
    df['Purchase_Amount_USD'] = df['Purchase_Amount_USD'].clip(lower=0)

if 'Review_Rating' in df.columns:
    df['Review_Rating'] = df['Review_Rating'].clip(lower=0, upper=5)

if 'Previous_Purchases' in df.columns:
    df['Previous_Purchases'] = df['Previous_Purchases'].clip(lower=0)

# Save cleaned dataset
df.to_csv(r"C:\Users\Vaishnavi\Documents\Visual Studio 18\Customer_shipping_behaviour\Python file\Data\Processed\cleaned_consumer_behavior.csv", index=False)

print("\nCleaned Shape:", df.shape)
df.head()
print("Cleaned dataset saved successfully.")