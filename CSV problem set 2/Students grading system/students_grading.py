import csv
from collections import defaultdict

FILENAME = "grades.csv"

# Initialize CSV file with headers if not present
def initialize_file():
    try:
        with open(FILENAME, "x", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student", "Subject", "Grade"])
    except FileExistsError:
        pass  # File already exists

# Add a new grade
def add_grade(student, subject, grade):
    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student, subject, grade])
    print(" Grade added successfully.")

# View all grades
def view_all_grades():
    print("\n All Grades:")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Calculate and display average grades per student
def calculate_averages():
    grades = defaultdict(list)

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = row["Student"]
            try:
                grade = float(row["Grade"])
                grades[student].append(grade)
            except ValueError:
                continue  # skip invalid data

    if grades:
        print("\n Average Grades:")
        for student, values in grades.items():
            avg = sum(values) / len(values)
            print(f"{student}: {avg:.2f}")
    else:
        print(" No grade records found.")

# Sort students by average grade
def sort_by_average():
    grades = defaultdict(list)

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = row["Student"]
            try:
                grade = float(row["Grade"])
                grades[student].append(grade)
            except ValueError:
                continue

    if not grades:
        print(" No data to sort.")
        return

    averages = [(student, sum(g) / len(g)) for student, g in grades.items()]
    sorted_averages = sorted(averages, key=lambda x: x[1], reverse=True)

    print("\n Students Sorted by Average Grade:")
    for student, avg in sorted_averages:
        print(f"{student}: {avg:.2f}")

# View subjects and grades for a specific student
def view_student_details(student_name):
    found = False
    print(f"\n Subjects and Grades for {student_name}:")
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Student'].lower() == student_name.lower():
                print(f"{row['Subject']}: {row['Grade']}")
                found = True
    if not found:
        print(" No records found for this student.")

# Display menu
def menu():
    print("""
=====  Student Grade Manager =====
1.  Add Grade
2.  View All Grades
3.  Calculate Average Grades
4. Sort Students by Average Grade
5.  View Student Details
6.  Exit
""")

# Main loop
def main():
    initialize_file()

    while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            student = input("Enter student name: ")
            subject = input("Enter subject: ")
            while True:
                try:
                    grade = float(input("Enter grade (0-100): "))
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
            add_grade(student, subject, grade)

        elif choice == '2':
            view_all_grades()

        elif choice == '3':
            calculate_averages()

        elif choice == '4':
            sort_by_average()

        elif choice == '5':
            student = input("Enter student name: ")
            view_student_details(student)

        elif choice == '6':
            print(" Exiting. Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
