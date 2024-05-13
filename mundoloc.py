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
# sample


# Routes for querying artists, songs, and albums
@app.route('/artists')
def get_artists():
    return jsonify(artists)

    # Routes for querying artists, songs, and albums
@app.route('/songs')
def get_songs():
    return jsonify(songs)


if __name__ == '__main__':
    app.run(debug=True)
