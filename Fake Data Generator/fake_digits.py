import random
import matplotlib.pyplot as plt
from faker import Faker
import pandas as pd

print("this will produce random float number : ")
print(random.random())

print("\nthis will produce float number between the given limit : ")
print(random.uniform(10,50))

print("\n this will produce int number between limits : ")
print(random.randint(10,40))

print("\n this will produce different integers at intervals : ")
print(random.randrange(0, 100, 10))

print("\n it will print normal distrbution : ")
print(random.gauss(10,3))

normal = [random.gauss(10,3) for _ in range (100)]
plt.hist(normal)
#plt.show()

directions = ["E", "W", "N", "S"]
print("\n choosing random value from list : ")
print(random.choice(directions))

print("Reproducing same random values wih the help of seed : ")
random.seed(1)
print(random.random())

locale_list = ['en-us', 'de-DE']
locale_fake = Faker(locale_list)
locale_fake.name()

def generate_person():
    return{
        "Name" : locale_fake.name(),
        "Job" : locale_fake.job(),
        "Address" : locale_fake.address(), 
        "Phone" : locale_fake.phone_number(),
        "Email" : locale_fake.email()

    }

values = [generate_person() for _ in range(10)]
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)  # makes output adjust to screen size
pd.set_option('display.max_colwidth', None)  # shows full content in each column


print(pd.DataFrame(values))



