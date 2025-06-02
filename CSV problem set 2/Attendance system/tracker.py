import csv
import os
from datetime import datetime

CSV_FILE = "attendance.csv"

def init_csv():

    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "EmployeeID", "Status"])


def add_attendance(date, emp_id, status):
    
    status = status.capitalize()
    if status not in ["Present", "Absent"]:
        print("Invalid status. Use 'Present' or 'Absent'.")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    # Check for duplicates
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == date and row[1] == emp_id:
                print("Duplicate record found. Entry not added.")
                return

    # Write new attendance
    with open(CSV_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, emp_id, status])
    print("Attendance recorded successfully.")


def generate_report():
    
    attendance = {}
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            emp_id = row["EmployeeID"]
            status = row["Status"]
            if emp_id not in attendance:
                attendance[emp_id] = 0
            if status.lower() == "present":
                attendance[emp_id] += 1

    if attendance:
        print("\nAttendance Report:")
        for emp_id, count in attendance.items():
            print(f"EmployeeID: {emp_id} - Days Present: {count}")
    else:
        print("No records found.")


def menu():
    
    while True:
        print("\nEmployee Attendance Tracker")
        print("1. Add Attendance")
        print("2. Generate Report")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            emp_id = input("Enter Employee ID: ")
            status = input("Enter Status (Present/Absent): ")
            add_attendance(date, emp_id, status)

        elif choice == '2':
            generate_report()

        elif choice == '3':
            print("Exiting Attendance Tracker. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Start the app
if __name__ == "__main__":
    init_csv()
    menu()
