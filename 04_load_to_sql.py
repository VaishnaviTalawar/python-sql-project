import pandas as pd
from sqlalchemy import create_engine, text
import urllib
import os

# ---------------------------------------
# Load transformed dataset
# ---------------------------------------
df = pd.read_csv(r"C:\Users\Vaishnavi\Documents\Visual Studio 18\Customer_shipping_behaviour\Python file\Data\Processed\cleaned_consumer_behavior.csv")

print("Original Columns:")
print(df.columns.tolist())

# ---------------------------------------
# Rename columns to match SQL table names
# ---------------------------------------
df = df.rename(columns={
    "Customer ID": "Customer_ID",
    "Item Purchased": "Item_Purchased",
    "Purchase Amount (USD)": "Purchase_Amount_USD",
    "Review Rating": "Review_Rating",
    "Subscription Status": "Subscription_Status",
    "Shipping Type": "Shipping_Type",
    "Discount Applied": "Discount_Applied",
    "Promo Code Used": "Promo_Code_Used",
    "Previous Purchases": "Previous_Purchases",
    "Payment Method": "Payment_Method",
    "Frequency of Purchases": "Frequency_of_Purchases",
    "Age Group": "Age_Group",
    "Spending Segment": "Spending_Segment",
    "Loyalty Segment": "Loyalty_Segment",
    "Review Category": "Review_Category",
    "Subscription Flag": "Subscription_Flag",
    "Discount Flag": "Discount_Flag",
    "Promo Used Flag": "Promo_Used_Flag",
    "Purchase Frequency Score": "Purchase_Frequency_Score",
    "Customer Satisfaction Segment": "Customer_Satisfaction_Segment"
})

# ---------------------------------------
# Clean Customer_ID
# ---------------------------------------
df["Customer_ID"] = pd.to_numeric(df["Customer_ID"], errors="coerce")
df = df.dropna(subset=["Customer_ID"])
df["Customer_ID"] = df["Customer_ID"].astype(int)

# ---------------------------------------
# SQL Server connection
# ---------------------------------------
server = r'LAPTOP-Q5MO66SO\SQLEXPRESS'
database = 'CustomerShoppingDB'

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# ---------------------------------------
# Create Products table dataframe
# ---------------------------------------
products = df[['Item_Purchased', 'Category', 'Size', 'Color']].drop_duplicates().reset_index(drop=True)

# ---------------------------------------
# Customers table
# ---------------------------------------
customers = df[[
    'Customer_ID', 'Age', 'Age_Group', 'Gender', 'Location',
    'Subscription_Status', 'Subscription_Flag',
    'Previous_Purchases', 'Loyalty_Segment'
]].copy()

customers = customers.sort_values("Customer_ID")
customers = customers.groupby("Customer_ID", as_index=False).first()

# ---------------------------------------
# Debug checks
# ---------------------------------------
print("\nCustomers duplicate check:")
print(customers["Customer_ID"].duplicated().sum(), "duplicate IDs")

print("\nRows to insert:")
print("Customers:", len(customers))
print("Products:", len(products))

# Save debug copies
os.makedirs("outputs", exist_ok=True)
customers.to_csv("outputs/customers_debug.csv", index=False)
products.to_csv("outputs/products_debug.csv", index=False)

# ---------------------------------------
# Load Customers and Products into SQL
# ---------------------------------------
customers.to_sql('Customers', engine, if_exists='append', index=False)
products.to_sql('Products', engine, if_exists='append', index=False)

print("\nCustomers and Products loaded successfully!")

# ---------------------------------------
# Fetch Product_ID from SQL and merge back
# ---------------------------------------
products_sql = pd.read_sql("""
    SELECT Product_ID, Item_Purchased, Category, Size, Color
    FROM Products
""", engine)

df = df.merge(products_sql, on=['Item_Purchased', 'Category', 'Size', 'Color'], how='left')

# ---------------------------------------
# Transactions table
# DO NOT include Transaction_ID (SQL will auto create it)
# ---------------------------------------
transactions = df[[
    'Customer_ID', 'Product_ID', 'Purchase_Amount_USD', 'Season',
    'Shipping_Type', 'Discount_Applied', 'Discount_Flag',
    'Promo_Code_Used', 'Promo_Used_Flag', 'Payment_Method',
    'Frequency_of_Purchases'
]].copy()

# ---------------------------------------
# Reviews table
# DO NOT include Review_ID (SQL will auto create it)
# ---------------------------------------
reviews = df[[
    'Customer_ID', 'Product_ID', 'Review_Rating', 'Review_Category'
]].copy()

print("Transactions:", len(transactions))
print("Reviews:", len(reviews))

transactions.to_csv("outputs/transactions_debug.csv", index=False)
reviews.to_csv("outputs/reviews_debug.csv", index=False)

# ---------------------------------------
# Load Transactions and Reviews into SQL
# ---------------------------------------
transactions.to_sql('Transactions', engine, if_exists='append', index=False)
reviews.to_sql('Reviews', engine, if_exists='append', index=False)

print("\nData loaded successfully into SQL Server!")