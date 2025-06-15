#API INTEGRATION AND DATA VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: SANIKA VYAS

INTERN ID:CT04DN249

DOMAIN: PYTHON 

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION OF CODE:
This Python script is designed to collect and visualize movie rating data from the Open Movie Database (OMDb) using their public API. It effectively combines the power of four major Python libraries: requests, pandas, matplotlib, and seaborn to create a simple yet complete data pipeline. The primary goal of the code is to automate the process of retrieving essential movie information such as title, year of release, IMDb rating, and genre, store it in a structured format, and present the ratings visually using a bar chart. This kind of task is highly useful in real-world applications like data journalism, entertainment analytics, dashboard development, or learning projects for students of programming and data science.

The code starts by importing the required libraries. requests is used for making HTTP GET requests to the OMDb API and getting responses in JSON format. It allows the script to connect to external servers over the web, making it essential for interacting with public APIs. The second library, pandas, is a high-performance data manipulation tool. It helps convert the raw JSON data into a DataFrame—a table-like structure—which simplifies data handling, filtering, and analysis. matplotlib.pyplot, one of the most widely used plotting libraries in Python, provides the basic functionality needed to create plots and charts. Finally, seaborn is used on top of matplotlib to generate cleaner, more modern, and statistically styled visualizations with minimal effort.

The script defines a list of movie titles that the user wants to search in the OMDb database. These movie titles include both Bollywood and Hindi-English crossover films such as "Dangal," "Jawan," and "The Sky is Pink." The code uses a loop to iterate through this list, and for each movie, it constructs a query URL by embedding the movie title and the API key into the endpoint. Using the requests.get() function, the script sends an HTTP request to the OMDb API, which returns a JSON object. This object contains various movie details like title, year, ratings, genre, cast, plot summary, and more.

To ensure the script is robust, it checks whether the response from the OMDb API was successful (i.e., "Response": "True"). If the movie is found in the database, the code extracts selected fields such as the title, year, IMDb rating, and genre. The IMDb rating is carefully parsed—checking if the rating is not "N/A"—before converting it to a float, ensuring the data remains clean and usable for numerical analysis. These fields are then appended to a list of dictionaries. If the movie is not found, a message is printed to inform the user.

Once data collection is complete, the script uses pandas to convert the list of movie information into a DataFrame. This tabular format allows for easy inspection and sets the stage for visualization. The DataFrame is printed, displaying the titles, release years, genres, and IMDb ratings of the movies that were successfully found.

The visualization step begins by setting up a figure with a specific size using matplotlib. A horizontal bar chart is created using seaborn's barplot() function, where the X-axis represents IMDb ratings and the Y-axis lists the movie titles. The plot is styled with the “rocket” color palette for better visual appeal. Titles and axis labels are added to ensure the chart is informative and visually accessible. The tight_layout() function adjusts the spacing to prevent overlapping text, and plt.show() renders the final plot.

In real-world scenarios, this script can be expanded in many useful ways. It can serve as the backend for a web app that displays real-time movie data. It could also be used in analytics tools to compare movie performances by genre or director. For students, this script is an excellent introduction to working with APIs, handling JSON, using pandas for data wrangling, and building meaningful visualizations. Its modular design allows for easy enhancement, such as sorting by rating, filtering by genre, or adding new fields like box office collection or runtime.



OUTPUT OF CODE:
![Image](https://github.com/user-attachments/assets/4a6269f8-bc77-4489-9973-1839625aa427)



