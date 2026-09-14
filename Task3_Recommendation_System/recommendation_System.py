import pandas as pd

# Load dataset
movies = pd.read_csv("movies.csv")

print("========== Movie Recommendation System ==========")

# Display available genres
genres = movies["Genre"].unique()

print("\nAvailable Genres:")
for i, genre in enumerate(genres, start=1):
    print(f"{i}. {genre}")

choice = input("\nEnter your favorite genre: ").strip()

# Recommend movies
recommended = movies[movies["Genre"].str.lower() == choice.lower()]

print("\nRecommended Movies:\n")

if len(recommended) == 0:
    print("Sorry! No recommendations found.")
else:
    for movie in recommended["Movie"]:
        print("✔", movie)

print("\nThank you for using the Recommendation System!")