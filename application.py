from flask import Flask, jsonify

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

if __name__ == '__main__':
    # Set the port to 80
    port = 80
    app.run(host='0.0.0.0', port=port)
    
  
