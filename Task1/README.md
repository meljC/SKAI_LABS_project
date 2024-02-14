
## Task 1: Display Polygon on a Map

### Overview

The goal of this task is to create a web application that displays a polygon, defined in a provided JSON file, on a map using the OpenLayers library. The application fetches polygon coordinates from a Flask server and displays the polygon on a map, ensuring the map centers on the polygon and adjusts its zoom to make the entire polygon visible.

### Technologies Used

- Python with Flask for the backend server
- JavaScript with OpenLayers for frontend map display

### How to Run

1. **Set up the Flask server:**
   - Ensure you have Python installed on your system.
   - Install Flask using `pip install Flask`.
   - Run the server using `python app.py`.

2. **Accessing the Application:**
   - Open a web browser and go to `http://localhost:5000` to view the application.

### Assumptions and Decisions

- The polygon coordinates are served from a static JSON file using Flask.
- OpenLayers is used for displaying the map due to its flexibility and compatibility with various map sources and formats.

For any questions or further information, feel free to contact me at dmeljanac@gmail.com.

