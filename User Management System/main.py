import json
import os

FILE_NAME = "user_data.json"

def load_users():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME , "r") as file:
        return json.load(file)


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent= 4)

def add_user(username, email, preferences):
    users = load_users()

    for user in users:
        if user["username"] == username or user["email"] == email:
            print("User already exists")
            return

    new_user = {
        "username": username,
        "email": email,
        "preferences": preferences
    }

    users.append(new_user)
    save_users(users)
    print("User successfully added.")


def update_user(username, updated_data):
    users = load_users()

    for user in users:
        if user["username"] == username:
            user.update(updated_data)
            save_users(users)
            print("User updated successfully.")
            return

    print("User not found.")

def delete_user(username):
    users = load_users()
    new_list = []

    found = False
    for user in users:
        if user["username"] == username:
            found = True
            continue
        new_list.append(user)

    if not found:
        print("user not found")
    else:
        save_users(new_list)
        print("user deleted succesfully")

def get_user(identifier):
    users = load_users()

    for user in users:
        if user["username"] == identifier or user["email"] == identifier:
            return user 

    return None

def print_user(user):
    if user is None:
        print("user not found")
    else:
        print("\n user details : ")
        print("username : ",user["username"])
        print("Email : ", user["email"])
        print("preferences : ",user["preferences"])     


def menu():
    while True:
        print("\n🔧 User Management Menu")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Get User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            theme = input("Preferred theme (light/dark): ")
            notify = input("Enable notifications? (yes/no): ")
            preferences = {
                "theme": theme,
                "notifications": notify.lower() == "yes"
            }
            add_user(username, email, preferences)

        elif choice == "2":
            username = input("Enter username to update: ")
            field = input("What do you want to update? (email/theme/notifications): ").strip().lower()
            value = input("Enter new value: ").strip()

            if field == "notifications":
                value = value.lower() == "yes"

            if field == "email":
                update_user(username, {"email": value})
            elif field in ["theme", "notifications"]:
                update_user(username, {"preferences": {field: value}})
            else:
                print("Invalid field. Only email, theme, or notifications can be updated.")


        elif choice == "3":
            username = input("Enter username to delete: ")
            delete_user(username)

        elif choice == "4":
            identifier = input("Enter username or email to find user: ")
            user = get_user(identifier)
            print_user(user)

        elif choice == "5":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    menu()




