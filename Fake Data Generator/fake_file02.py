from faker import Faker
import pandas as pd

fake = Faker(locale= 'en_us')
employee_List = []
def dummy_data(records):
    for _ in range(records):
        employee = {}
        employee['First name'] = fake.first_name()
        employee['Last name'] = fake.last_name()
        employee['Job'] = fake.job()
        employee['Department'] = fake.random_element(elements=  ["IT", "HR", "Marketing", "Finance" ])
        employee['Role'] = fake.random_element(elements= ["Analyst", "Manager", "Associate", "Developer" ])
        employee['Salary'] = fake.random_int(min= 40000, max= 1000000, step= 1000)
        employee['Email'] = fake.email()
        employee_List.append(employee)
    return pd.DataFrame(employee_List)

records = int(input("enter how many employees data you want ? "))
result = dummy_data(records)
result.to_csv("fake_data02.csv",index=False)
print(result.to_string(index= False))


