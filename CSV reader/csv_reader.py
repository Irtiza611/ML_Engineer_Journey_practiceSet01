import csv

with open("person.csv") as f:
    reader = csv.reader(f, delimiter = ",")

    for line in reader:
        print(line)

print()
print("this is file reading when we dont ignore the spaces ")
with open("person_with_spaces.csv") as f:
    reader = csv.reader(f)

    for line in reader:
        print(line)

print()
print("this is file reading when we ignore the spaces ")
with open("person_with_spaces.csv") as f:
    reader = csv.reader(f, skipinitialspace = True)

    for line in reader:
        print(line)

print()
print("NOw with the use of DictReader you will see the results in Dictionary")
with open("person.csv") as f:
    reader = csv.DictReader(f)

    for line in reader:
        print(line)
