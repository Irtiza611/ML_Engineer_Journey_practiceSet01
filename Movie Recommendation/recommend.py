import json

data = [
  {
    "name": "Inception",
    "genre": "Science Fiction",
    "rating": 8
  },
  {
    "name": "The Shawshank Redemption",
    "genre": "Drama",
    "rating": 9
  },
  {
    "name": "The Godfather",
    "genre": "Crime",
    "rating": 9
  },
  {
    "name": "The Dark Knight",
    "genre": "Action",
    "rating": 9
  },
  {
    "name": "Pulp Fiction",
    "genre": "Crime",
    "rating": 8
  },
  {
    "name": "Forrest Gump",
    "genre": "Drama",
    "rating": 8
  },
  {
    "name": "The Matrix",
    "genre": "Science Fiction",
    "rating": 8
  },
  {
    "name": "Interstellar",
    "genre": "Science Fiction",
    "rating": 8
  },
  {
    "name": "Parasite",
    "genre": "Thriller",
    "rating": 8
  },
  {
    "name": "Gladiator",
    "genre": "Action",
    "rating": 8
  }
]


with open("movie_name.json", "w") as file:
    json.dump(data, file)


genre = input("enter the genre of movie : ").strip().title()
rating = int(input("enter the rating of movie : ").strip())

print(genre)
print(rating)

with open("movie_name.json") as file:
    movies = json.load(file) 

found = False
for movie in movies:
    if movie["genre"] == genre and movie["rating"] == rating:
        print(movie)
        found = True
        break

if not found:
    print("movie not found")




