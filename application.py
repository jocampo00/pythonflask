from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Sample data for artists, songs, and albums
artists = [
    {"id": 1, "name": "Vincent van Gogh"},
    {"id": 2, "name": "Pablo Picasso"},
    {"id": 3, "name": "Leonardo da Vinci"}
]

songs = [
    {"id": 1, "name": "ViAJAA dovan Gogh"},
    {"id": 2, "name": "Pablo Picasso"},
    {"id": 3, "name": "Leonardo da Vinci"}
]

# Routes for querying artists, songs, and albums
@app.route('/artists')
def get_artists():
    return jsonify(artists)

@app.route('/songs')
def get_songs():
    return jsonify(songs)

@app.route('/swagger.json')
def swagger_json():
    return jsonify(swagger_data)  # Replace `swagger_data` with your actual Swagger JSON data


# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Your Flask Application"
    }
)

# Register the Swagger UI blueprint with the app
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    # Set the port to 80
    port = 80
    app.run(host='0.0.0.0', port=port)
