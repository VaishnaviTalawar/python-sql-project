import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\Documents\Visual Studio 18\Customer_shipping_behaviour\Python file\Data\Processed\cleaned_consumer_behavior.csv")


print("Dataset Loaded Successfully")
print(df.head())
df.columns = df.columns.str.strip().str.replace(" ", "_")
# -------------------------------
# 1. Create Age Group
# -------------------------------
def age_group(age):
    if age < 20:
        return "Teen"
    elif age < 30:
        return "20s"
    elif age < 40:
        return "30s"
    elif age < 50:
        return "40s"
    else:
        return "50+"

df["Age Group"] = df["Age"].apply(age_group)

# -------------------------------
# 2. Create Spending Segment
# -------------------------------
def spending_segment(amount):
    if amount < 30:
        return "Low Spender"
    elif amount < 70:
        return "Medium Spender"
    else:
        return "High Spender"

df["Spending Segment"] = df["Purchase_Amount_USD"].apply(spending_segment)

# -------------------------------
# 3. Create Loyalty Segment
# Based on Previous Purchases
# -------------------------------
def loyalty_segment(purchases):
    if purchases < 10:
        return "New Customer"
    elif purchases < 25:
        return "Returning Customer"
    else:
        return "Loyal Customer"

df["Loyalty Segment"] = df["Previous_Purchases"].apply(loyalty_segment)

# -------------------------------
# 4. Create Review Category
# -------------------------------
def review_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 3.5:
        return "Good"
    elif rating >= 2.5:
        return "Average"
    else:
        return "Poor"

df["Review Category"] = df["Review_Rating"].apply(review_category)

# -------------------------------
# 5. Convert Yes/No columns to Flags
# -------------------------------
df["Subscription Flag"] = df["Subscription_Status"].map({"Yes": 1, "No": 0})
df["Discount Flag"] = df["Discount_Applied"].map({"Yes": 1, "No": 0})
df["Promo Used Flag"] = df["Promo_Code_Used"].map({"Yes": 1, "No": 0})

# -------------------------------
# 6. Create Purchase Frequency Score
# -------------------------------
def frequency_score(freq):
    freq = str(freq).strip().lower()

    if "weekly" in freq:
        return 4
    elif "fortnightly" in freq:
        return 3
    elif "monthly" in freq:
        return 2
    elif "quarterly" in freq:
        return 1
    else:
        return 0

df["Purchase Frequency Score"] = df["Frequency_of_Purchases"].apply(frequency_score)

# -------------------------------
# 7. Customer Value Indicator
# -------------------------------
def customer_value(row):
    if row["Purchase_Amount_USD"] >= 70 and row["Previous_Purchases"] >= 20:
        return "High Value"
    elif row["Purchase_Amount_USD"] >= 40 and row["Previous_Purchases"] >= 10:
        return "Medium Value"
    else:
        return "Low Value"

# -------------------------------
# 8. Review + Purchase Behavior Segment
# -------------------------------
def satisfaction_segment(row):
    if row["Review_Rating"] >= 4 and row["Previous_Purchases"] >= 20:
        return "Satisfied Loyal"
    elif row["Review_Rating"] < 3 and row["Previous_Purchases"] < 10:
        return "At Risk"
    else:
        return "Normal"

df["Customer Satisfaction Segment"] = df.apply(satisfaction_segment, axis=1)

# -------------------------------
# Save Updated Dataset
# -------------------------------
df.to_csv(r"C:\Users\Vaishnavi\Documents\Visual Studio 18\Customer_shipping_behaviour\Python file\Data\Processed\cleaned_consumer_behavior.csv", index=False)

print("\nFeature Engineering Completed Successfully!")
print("\nNew Columns Added:")
print([
    "Age Group",
    "Spending Segment",
    "Loyalty Segment",
    "Review Category",
    "Subscription Flag",
    "Discount Flag",
    "Promo Used Flag",
    "Purchase Frequency Score",
    "Customer Value Segment",
    "Customer Satisfaction Segment"
])

print("\nUpdated Dataset Preview:")
print(df.head())