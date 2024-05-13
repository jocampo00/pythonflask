from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

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
@app.route('/artists', methods=['GET'])
def get_artists():
    """
    Retrieve a list of artists.
    ---
    responses:
      200:
        description: A list of artists.
    """
    return jsonify(artists)

@app.route('/songs', methods=['GET'])
def get_songs():
    """
    Retrieve a list of songs.
    ---
    responses:
      200:
        description: A list of songs.
    """
    return jsonify(songs)

if __name__ == '__main__':
    # Set the port to 80
    port = 80
    app.run(host='0.0.0.0', port=port)


          
          Expand Down
    
    
  
    app.run(host='0.0.0.0', port=port)
