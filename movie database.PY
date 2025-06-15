import requests    # To send HTTP requests and get movie data from the OMDb API
import pandas as pd   # For creating and managing tabular data (DataFrame)
import matplotlib.pyplot as plt  # For creating plots
import seaborn as sns   # For making visually appealing statistical graphics

api_key ="237e74dc"    # API key to access OMDb API 

# List of movie titles to search for
movies_to_search = ["The Sky is Pink","Raid 2","Roy","Saawariya","Dangal","Jawan","Players"]


movie_data = []  # Empty list to store data for each movie

# Loop through each movie title
for title in movies_to_search:

 # Construct the URL to query the OMDb API for each movie
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)  # Send HTTP GET request
    data = response.json()       # Convert response to JSON

# Check if movie was found in the OMDb database
    if data["Response"] == "True":
        movie_data.append({             # Append useful information to movie_data
            "Title": data["Title"],
            "Year": data["Year"],
            "IMDb Rating": float(data["imdbRating"]) if data["imdbRating"] != "N/A" else None,

            "Genre": data["Genre"]
        })
    else:
        print(f"Movie '{title}'not found ")    # Print error if movie not found


# Create a pandas DataFrame from the collected movie data
df = pd.DataFrame(movie_data)

print(df)   # Print the DataFrame to view the data collected

# Visualization: IMDb Ratings using a horizontal bar chart
plt.figure(figsize=(10,6))  # Set figure size
sns.barplot(data=df, x="IMDb Rating",y = "Title", palette="rocket")    # Create barplot
plt.title("IMDb Rating of Top Movies ")    # Add title
plt.xlabel("Rating")    # X-axis label
plt.ylabel("Movies")   # Y-axis label
plt.tight_layout()      # Adjust layout to avoid overlap
plt.show()              # Display the plot
