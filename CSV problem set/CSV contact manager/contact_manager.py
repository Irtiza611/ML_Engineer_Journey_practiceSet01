import csv
import pandas as pd
import os


def add_contact(name, phone, email):
    with open("contacts.csv", "a", newline = '')as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
        
    print("Contact added successfully")

def read_contacts():
    df = pd.read_csv("contacts.csv")
    print(df)

def search_contact(keyword):
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        #headers = next(reader)  # skip header row
        for row in reader:
            if keyword.lower() in row[0].lower() or keyword.lower() in row[2].lower():
                print("Match found:", row)
                return
        print("No contact found.")


def update_contact(keyword, new_name, new_phone, new_email):
    contacts = []
    updated = False
    with open("contacts.csv","r")as file:
        reader = csv.reader(file)
        for row in reader: 
            if keyword.lower() in row[0].lower() or keyword.lower() in row[2].lower():
                contacts.append([new_name, new_phone, new_email])
                updated = True
            else:
                contacts.append(row)

    with open("contacts.csv","w",newline = '')as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

    if updated:
        print("COntacts updated")
    else:
        print("Contact not found")

def delete_contact(keyword):
    contacts = []
    deleted = False

    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if keyword.lower() in row[0].lower() or keyword.lower() in row[2].lower():
                deleted = True
                continue
            contacts.append(row)

    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

    if deleted:
        print("Contact deleted.")
    else:
        print("Contact not found.")



def menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


while True:
    menu()
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)

    elif choice == '2':
        read_contacts()

    elif choice == '3':
        keyword = input("Enter name or email to search: ")
        search_contact(keyword)

    elif choice == '4':
        keyword = input("Enter name or email of contact to update: ")
        new_name = input("New name: ")
        new_phone = input("New phone: ")
        new_email = input("New email: ")
        update_contact(keyword, new_name, new_phone, new_email)

    elif choice == '5':
        keyword = input("Enter name or email of contact to delete: ")
        delete_contact(keyword)

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid option. Try again.")

