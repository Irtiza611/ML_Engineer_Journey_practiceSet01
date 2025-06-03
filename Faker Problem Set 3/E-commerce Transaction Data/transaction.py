from faker import Faker
import pandas as pd
import numpy as np
from random import randint, choice
from datetime import datetime

fake = Faker()
Faker.seed(42)
np.random.seed(42)

product_catalog = [
    {"name": "Wireless Mouse", "category": "Electronics", "price": 19.99},
    {"name": "Bluetooth Headphones", "category": "Electronics", "price": 49.99},
    {"name": "Yoga Mat", "category": "Fitness", "price": 25.00},
    {"name": "Running Shoes", "category": "Footwear", "price": 60.00},
    {"name": "Coffee Maker", "category": "Home Appliances", "price": 89.99},
    {"name": "Desk Lamp", "category": "Furniture", "price": 29.99},
    {"name": "Backpack", "category": "Accessories", "price": 45.00},
    {"name": "T-shirt", "category": "Clothing", "price": 15.00},
]

payment_methods = ["Credit Card", "PayPal", "Cash on Delivery", "Bank Transfer"]


def generate_transactions(n=10):
    data = []

    for i in range(1, n + 1):
        product = choice(product_catalog)
        quantity = randint(1, 5)
        total = round(quantity * product["price"], 2)

        transaction = {
            "Transaction ID": f"T{i:05d}",
            "Product Name": product["name"],
            "Category": product["category"],
            "Quantity": quantity,
            "Price (Each)": product["price"],
            "Total Amount": total,
            "Customer Name": fake.name(),
            "Email": fake.email(),
            "Address": fake.address().replace("\n", ", "),
            "Purchase Date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "Payment Method": choice(payment_methods)
        }

        data.append(transaction)

    return pd.DataFrame(data)

# Save to CSV
def export_to_csv(df, filename="ecommerce_transactions.csv"):
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

# Basic Analysis
def analyze_data(df):
    print("\n📊 Basic Data Analysis:\n")

    
    total_revenue = df["Total Amount"].sum()
    print(f"Total Revenue: ${total_revenue:,.2f}")


    top_products = df.groupby("Product Name")["Quantity"].sum().sort_values(ascending=False).head(5)
    print("\nTop 5 Best-Selling Products:\n", top_products)

    
    popular_payment = df["Payment Method"].value_counts().head(3)
    print("\nMost Popular Payment Methods:\n", popular_payment)

    
    df["Month"] = pd.to_datetime(df["Purchase Date"]).dt.to_period("M")
    monthly_sales = df.groupby("Month")["Total Amount"].sum()
    print("\nMonthly Revenue:\n", monthly_sales)


if __name__ == "__main__":
    df = generate_transactions(10)  
    print(df.head()) 
    export_to_csv(df)
    analyze_data(df)
