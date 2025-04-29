# import pandas as pd
# import numpy as np

# # Creating Suppliers Table
# suppliers_data = {
#     "SupplierID": range(1, 6),
#     "SupplierName": ["Alpha Ltd", "Beta Inc", "Gamma Corp", "Delta LLC", "Epsilon Pvt"],
#     "Location": ["New York", "California", "Texas", "Florida", "Illinois"],
#     "Rating": np.random.randint(1, 6, size=5)  # Rating from 1 to 5
# }
# suppliers_df = pd.DataFrame(suppliers_data)

# # Creating Products Table
# products_data = {
#     "ProductID": range(101, 111),
#     "ProductName": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer",
#                     "Desk", "Chair", "Router", "Headphones", "Smartphone"],
#     "Category": ["Electronics"] * 5 + ["Furniture"] * 2 + ["Networking", "Accessories", "Electronics"],
#     "Price": np.random.randint(50, 1000, size=10),
#     # Randomly assign suppliers
#     "SupplierID": np.random.choice(suppliers_df["SupplierID"], size=10)
# }
# products_df = pd.DataFrame(products_data)

# # Creating Orders Table
# order_dates = pd.date_range(start="2024-01-01", periods=15, freq="D")
# orders_data = {
#     "OrderID": range(1001, 1016),
#     "ProductID": np.random.choice(products_df["ProductID"], size=15),
#     "Quantity": np.random.randint(1, 10, size=15),
#     "OrderDate": np.random.choice(order_dates, size=15),
#     "DeliveryStatus": np.random.choice(["Delivered", "Pending", "Cancelled"], size=15, p=[0.6, 0.3, 0.1])
# }
# orders_df = pd.DataFrame(orders_data)

# # Displaying the tables
# print("Suppliers Table:")
# print(suppliers_df)
# print("\nProducts Table:")
# print(products_df)
# print("\nOrders Table:")
# print(orders_df)

# # Save to CSV for later use
# suppliers_df.to_csv("suppliers.csv", index=False)
# products_df.to_csv("products.csv", index=False)
# orders_df.to_csv("orders.csv", index=False)


import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset (Make sure you have the CSVs)
products_df = pd.read_csv("products.csv")
orders_df = pd.read_csv("orders.csv")
suppliers_df = pd.read_csv("suppliers.csv")

# Step 2: Preview Data
print("\n🟢 First 5 rows of Products:")
print(products_df.head())

print("\n🔵 First 5 rows of Orders:")
print(orders_df.head())

print("\n🟠 First 5 rows of Suppliers:")
print(suppliers_df.head())

# Step 3: Merge Orders with Products
merged_df = pd.merge(orders_df, products_df, on='ProductID', how='inner')

# Step 4: Merge with Suppliers
final_df = pd.merge(merged_df, suppliers_df, on='SupplierID', how='left')

print("\n🟣 Merged Data (Orders + Products + Suppliers):")
print(final_df.head())

# Step 5: Total Revenue per Product
final_df['Total_Revenue'] = final_df['Quantity'] * final_df['Price']

revenue_per_product = final_df.groupby(
    'ProductName')['Total_Revenue'].sum().reset_index()
print("\n📌 Total Revenue per Product:")
print(revenue_per_product.sort_values('Total_Revenue', ascending=False))

# Step 6: Find Most Sold Products
top_selling_products = final_df.groupby(
    'ProductName')['Quantity'].sum().reset_index()
top_selling_products = top_selling_products.sort_values(
    'Quantity', ascending=False)
print("\n🔥 Top Selling Products:")
print(top_selling_products.head(5))

# Step 7: Find Products with Lowest Sales
print("\n📉 Products with Lowest Sales:")
print(top_selling_products.tail(5))

# Step 8: Count of Orders per Supplier
orders_per_supplier = final_df.groupby(
    'SupplierName')['OrderID'].nunique().reset_index()
print("\n🏭 Number of Orders per Supplier:")
print(orders_per_supplier.sort_values('OrderID', ascending=False))

# Step 9: Handling Missing Values
print("\n🛠 Checking for Missing Values:")
print(final_df.isnull().sum())

# Fill missing Supplier Names with "Unknown"
final_df['SupplierName'].fillna("Unknown", inplace=True)

# Step 10: Removing Duplicate Entries (if any)
final_df.drop_duplicates(inplace=True)

# Step 11: Find the Most Profitable Supplier
supplier_revenue = final_df.groupby(
    'SupplierName')['Total_Revenue'].sum().reset_index()
print("\n💰 Most Profitable Suppliers:")
print(supplier_revenue.sort_values('Total_Revenue', ascending=False).head(3))

# Step 12: Data Visualization (Bar Chart of Top 5 Products by Revenue)
plt.figure(figsize=(10, 5))
plt.bar(revenue_per_product['ProductName'].head(
    5), revenue_per_product['Total_Revenue'].head(5), color='blue')
plt.xlabel("Products")
plt.ylabel("Total Revenue")
plt.title("Top 5 Products by Revenue")
plt.xticks(rotation=45)
plt.show()

# Step 13: Data Visualization (Bar Chart of Orders per Supplier)
plt.figure(figsize=(10, 5))
plt.bar(orders_per_supplier['SupplierName'].head(
    5), orders_per_supplier['OrderID'].head(5), color='green')
plt.xlabel("Suppliers")
plt.ylabel("Total Orders")
plt.title("Top 5 Suppliers by Order Count")
plt.xticks(rotation=45)
plt.show()

print("\n✅ Pandas Practice Completed Successfully! 🎯")
