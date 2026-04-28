import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Vaishnavi\Documents\Visual Studio 18\Customer_shipping_behaviour\Python file\Data\Processed\cleaned_consumer_behavior.csv")

print("\n--- Top Categories by Sales ---")
print(df.groupby("Category")["Purchase_Amount_USD"].sum().sort_values(ascending=False))

print("\n--- Payment Method Usage ---")
print(df["Payment_Method"].value_counts())

print("\n--- Seasonal Sales ---")
print(df.groupby("Season")["Purchase_Amount_USD"].sum())

print("\n--- Subscription Status vs Spending ---")
print(df.groupby("Subscription_Status")["Purchase_Amount_USD"].mean())

# Chart 1
category_sales = df.groupby("Category")["Purchase_Amount_USD"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Chart 2
Payment_Count=print(df["Payment_Method"].value_counts())

plt.figure()
Payment_Count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Payment Method Usage")
plt.show()

#Chart 3
season_sales = df.groupby("Season")["Purchase_Amount_USD"].sum()

plt.figure()
season_sales.plot(kind='bar')
plt.title("Seasonal Sales")
plt.xlabel("Season")
plt.ylabel("Total Sales (USD)")
plt.show()

#Chart 4
subscription_spending = df.groupby("Subscription_Status")["Purchase_Amount_USD"].mean()

plt.figure()
subscription_spending.plot(kind='bar')
plt.title("Average Spending by Subscription Status")
plt.xlabel("Subscription Status")
plt.ylabel("Average Spending (USD)")
plt.show()

#Chart 5
plt.figure()
plt.hist(df["Purchase_Amount_USD"], bins=20)
plt.title("Purchase Amount Distribution")
plt.xlabel("Amount (USD)")
plt.ylabel("Frequency")
plt.show()

#chart 6
category_count = df["Category"].value_counts()

plt.figure()
category_count.plot(kind='bar')
plt.title("Number of Purchases per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
