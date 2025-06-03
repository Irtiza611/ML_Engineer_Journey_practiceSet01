import pandas as pd
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt


fake = Faker()
Faker.seed(42)
np.random.seed(42)


NUM_EMPLOYEES = 20
NUM_DEPARTMENTS = 5
NUM_PRODUCTS = 10
YEARS = [2019, 2020, 2021, 2022, 2023]

departments = [fake.job().split()[0] + " Dept" for _ in range(NUM_DEPARTMENTS)]
departments = list(set(departments))  


employees = []
for _ in range(NUM_EMPLOYEES):
    name = fake.name()
    department = np.random.choice(departments)
    job_title = fake.job()
    salary = np.random.randint(40000, 120000)
    employees.append({
        'EmployeeName': name,
        'Department': department,
        'JobTitle': job_title,
        'Salary': salary
    })

df_employees = pd.DataFrame(employees)

# Generate revenue data by year
revenue_data = []
for year in YEARS:
    revenue = np.random.randint(1_000_000, 5_000_000)
    revenue_data.append({'Year': year, 'Revenue': revenue})

df_revenue = pd.DataFrame(revenue_data)

# Generate product sales data
products = [f"Product_{i+1}" for i in range(NUM_PRODUCTS)]
product_sales = []
for product in products:
    for year in YEARS:
        units_sold = np.random.randint(500, 5000)
        sales_amount = units_sold * np.random.uniform(10, 100)  # price between $10 and $100
        product_sales.append({
            'Product': product,
            'Year': year,
            'UnitsSold': units_sold,
            'SalesAmount': sales_amount
        })

df_product_sales = pd.DataFrame(product_sales)


# 1. Number of Employees per Department (Horizontal Bar Chart)
dept_counts = df_employees['Department'].value_counts()
plt.figure(figsize=(8,6))
plt.barh(dept_counts.index, dept_counts.values, color='skyblue')
plt.xlabel('Number of Employees')
plt.ylabel('Department')
plt.title('Number of Employees per Department')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

# 2. Revenue Over Years (Line Chart)
plt.figure(figsize=(8,6))
plt.plot(df_revenue['Year'], df_revenue['Revenue'], marker='o', linestyle='-', color='green')
plt.title('Company Revenue Over Years')
plt.xlabel('Year')
plt.ylabel('Revenue (in dollars)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 3. Total Sales Amount per Product (Horizontal Bar Chart)
product_sales_sum = df_product_sales.groupby('Product')['SalesAmount'].sum().sort_values(ascending=True)
plt.figure(figsize=(10,6))
plt.barh(product_sales_sum.index, product_sales_sum.values, color='coral')
plt.xlabel('Sales Amount ($)')
plt.ylabel('Product')
plt.title('Total Sales Amount per Product')
plt.tight_layout()
plt.show()

# 4. Sales Trend of Top 3 Products Over Years (Line Chart)
top_products = product_sales_sum.sort_values(ascending=False).head(3).index.tolist()
plt.figure(figsize=(10,6))
for product in top_products:
    product_data = df_product_sales[df_product_sales['Product'] == product]
    plt.plot(product_data['Year'], product_data['SalesAmount'], marker='o', label=product)
plt.title('Sales Trends of Top 3 Products Over Years')
plt.xlabel('Year')
plt.ylabel('Sales Amount ($)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# === EXPORT TO CSV ===
df_employees.to_csv('fake_company_employees.csv', index=False)
df_revenue.to_csv('fake_company_revenue.csv', index=False)
df_product_sales.to_csv('fake_company_product_sales.csv', index=False)
