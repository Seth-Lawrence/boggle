from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    result = {"game_id":game_id,"board":game.board}

    return jsonify(result)
    #{"gameId": "need-real-id", "board": "need-real-board"}

@app.post("/api/score-word")
def score_word():
    """accepts a POST request with JSON for game id and word. Checks legality
    of word"""
    word = request.json["word"]
    return jsonify({"result":"okay"})





