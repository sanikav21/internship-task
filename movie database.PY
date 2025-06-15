import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api_key ="237e74dc"

movies_to_search = ["The Sky is Pink","Raid 2","Roy","Saawariya","Dangal","Jawan","Players"]


movie_data = []

for title in movies_to_search:
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        movie_data.append({
            "Title": data["Title"],
            "Year": data["Year"],
            "IMDb Rating": float(data["imdbRating"]) if data["imdbRating"] != "N/A" else None,

            "Genre": data["Genre"]
        })
    else:
        print(f"Movie '{title}'not found ")

df = pd.DataFrame(movie_data)

print(df)


plt.figure(figsize=(10,6))
sns.barplot(data=df, x="IMDb Rating",y = "Title", palette="rocket")
plt.title("IMDb Rating of Top Movies ")
plt.xlabel("Rating")
plt.ylabel("Movies")
plt.tight_layout()
plt.show()
