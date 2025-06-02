import csv
from collections import defaultdict

# Initialize the CSV file
column_header = ["Movie", "User", "Rating"]
row_data = [
    ["Inception", "Irtiza", "8"],
    ["Arcade", "Irtiza", "6"],
    ["Transformer", "Irtiza", "9"]
]

with open("record.csv", "w", newline='') as file:
    file_writer = csv.writer(file, delimiter=",")
    file_writer.writerow(column_header)
    file_writer.writerows(row_data)

# Function to add a rating
def add_rating(movie, user, rating):
    new_row = [movie, user, rating]
    with open("record.csv", "a", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        file_writer.writerow(new_row)
        print(" Rating has been added to records.")

# Calculate and display average ratings
def calculate_averages():
    ratings = defaultdict(list)

    with open("record.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = row["Movie"]
            rating = float(row["Rating"])
            ratings[movie].append(rating)

    if ratings:
        print("\n Average Ratings:")
        for movie, values in ratings.items():
            avg = sum(values) / len(values)
            print(f"{movie}: {avg:.2f}")
    else:
        print("No ratings found.")

# Find and display the top-rated movie
def find_top_rated_movie():
    ratings = defaultdict(list)

    with open("record.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = row["Movie"]
            rating = float(row["Rating"])
            ratings[movie].append(rating)

    if not ratings:
        print("No ratings to analyze.")
        return

    top_movie = max(ratings.items(), key=lambda x: sum(x[1]) / len(x[1]))
    avg = sum(top_movie[1]) / len(top_movie[1])
    print(f"\n Top Rated Movie: {top_movie[0]} with average rating {avg:.2f}")

# Main menu loop
while True:
    print("""
🎬 Movie Rating System:
    1. Add Rating
    2. View Average Ratings
    3. Show Top-Rated Movie
    4. Exit
""")
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print(" Please enter a valid number (1-4).")
        continue

    if option == 1:
        movie_name = input("Enter the name of the movie: ")
        user_name = input("Enter your name: ")
        ratings = input("Enter the rating of the movie (1 to 10): ")
        add_rating(movie_name, user_name, ratings)

    elif option == 2:
        calculate_averages()

    elif option == 3:
        find_top_rated_movie()

    elif option == 4:
        print(" Exiting! Thank you.")
        break

    else:
        print(" Invalid option. Try again.")
