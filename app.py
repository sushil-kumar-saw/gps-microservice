from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Classroom Location</title>
    </head>
    <body>

        <h1>Get My Classroom Location</h1>

        <button onclick="getLocation()">Get GPS Location</button>

        <p id="lat"></p>
        <p id="lon"></p>
        <p id="map"></p>

        <script>
        function getLocation() {
            document.getElementById("lat").innerHTML = "Latitude: 9.759288";
            document.getElementById("lon").innerHTML = "Longitude: 76.6528113";
            document.getElementById("map").innerHTML =
            '<a href="https://www.google.com/maps?q=9.759288,76.6528113" target="_blank">Open in Google Maps</a>';
        }
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
