import pandas as pd
import csv
import json

df = pd.read_csv("../Sales Data Analysis/sales_data.csv")
data = df.to_dict(orient = 'records')
print("The data in CSV format : ",df)
print()

with open("data.json","w") as file:
    json.dump(data, file, indent=4)

with open("data.json","r")as file:
    output = json.load(file)
    print("After conversion to JSON format the data will look like : ")
    print()
    print(json.dumps(output, indent=4))

