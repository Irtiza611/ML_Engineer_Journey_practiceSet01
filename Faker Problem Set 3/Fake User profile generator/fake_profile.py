from faker import Faker
fake = Faker()
import pandas as pd
import json

def generate_profiles(profile_count):
    profiles = []
    for _ in range(profile_count):
        profile = {
            "Name": fake.name(),
            "Email": fake.email(),
            "Phone": fake.phone_number(),
            "Address": fake.address().replace("\n", ", "),
            "DOB": fake.date_of_birth().isoformat(),
            "Job Title": fake.job(),
            "Company": fake.company(),
            "Username": fake.user_name(),
            "SSN": fake.ssn()
        }
        profiles.append(profile)
    return profiles

profiles = generate_profiles(profile_count=1000)
#this is the way to convert and save files into CSV format file
df = pd.DataFrame(profiles)
df.to_csv("records.csv", index= False)

#this is the way to convert and save files into JSON format file
with open("profile_records.json", "w")as file:
    json.dump(profiles, file, indent= 4 )

#now lets see the output of both files
read_csv = pd.read_csv("records.csv")
print(read_csv)
read_json = pd.read_json("profile_records.json")
print(read_json)
