import csv
import pandas
import matplotlib.pyplot as plt

columns_data = ["Date", "Product", "Quantity", "Price", "Region" ]
rows_data = [
    ["2025-01-01","Widget A","10","20","North"],
    ["2025-01-02","Widget B","5","50","South"],
    ["2025-01-03","Widget A","7","20","East"],
    ["2025-01-04","Widget C","3","30","West"],
    ["2025-01-05","Widget B","14","50","North"],
    ["2025-01-06","Widget C","6","30","South"]
]

with open("sales_data.csv","w", newline='') as f:
    file_writer = csv.writer(f, delimiter = ",")

    file_writer.writerow(columns_data)
    file_writer.writerows(rows_data)


df = pandas.read_csv("sales_data.csv")
print(df)

df["total"] = df['Quantity'] * df['Price']
total_sale = df["total"].sum()
print("Total sales will be : ", total_sale)


product_sales = df.groupby("Product")["Quantity"].sum()
most_sold_products = product_sales.idxmax()
print("Most sold item with refernce of Quantity is : ",most_sold_products)

product_sales_by_region = df.groupby("Region")["Quantity"].sum()
most_sold_products_by_region = product_sales_by_region.idxmax()
print("Most sold item with reference of region is : ",most_sold_products_by_region)

product_sales_by_region.plot(kind = "bar" ,title = "sales by region", ylabel = "total_sale")
plt.tight_layout()
plt.show()

product_sales.plot(kind = "pie", title = "sales by quantity", autopct = "%1.1f%%")
plt.ylabel("")
plt.tight_layout()
plt.show()
