from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

nameList = []
ageList = []
cnicList = []
cardNumList = []


def dummy_data(records):
    for _ in range(records):
        nameList.append(fake.name())

    for _ in range(records):
        ageList.append(np.random.randint(10,60))
        
    for _ in range(records):
        part1 = np.random.randint(10000, 99999)
        part2 = np.random.randint(1000000, 9999999)
        part3 = np.random.randint(0, 9)
        cnicList.append(f"{part1}-{part2}-{part3}")

    for _ in range(records):
        cardNumList.append(fake.credit_card_number())


    df = pd.DataFrame(zip(nameList, ageList, cnicList, cardNumList),columns= ["Name List", "Age List", "Cnic List", "Card Number List"])
    print(df.to_string(index= False))

records = int(input("How many fake records do you want to be generated? "))

dummy_data(records)
