from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<table class="board', html)
            self.assertIn('<title>Boggle</title>', html)
            self.assertIn('<!-- Hello world -->', html)


    def test_api_new_game(self):
        """Test starting a new game."""

        with app.test_client() as client:
            response = client.post('/api/new-game')
            game_data = response.get_json()
            gameID = game_data["game_id"]
            game_board = game_data["board"]

            # is there anything in the string
            # concat. + next index in the string
            letters_in_board = ""

            for list in game_board:
                letters_in_board += "".join(list) + "."

            letters_in_board = letters_in_board[:-1]


            print("letters_in_board=", letters_in_board)
            print("game data=",game_data)
            print("games=", games)

            self.assertTrue(game_data)
            self.assertEqual(len(game_data), 2)
            self.assertIn(gameID, games.keys())
            self.assertIn(letters_in_board, str(games[gameID]))








