from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from engine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

games = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('manual_turn')
def manualTurn(data):
    game_id = data['game_id']
    games[game_id].processCurrentTurn()
    
@socketio.on('get_game')
def get_game(data):
    game_id = data['game_id']
    player_name = data['player_name']
    
    if game_id not in games:
        player = Player(player_name, "Austria")
        games[game_id] = Game(create_gameState(), [player])

    pkg = games[game_id].getPackage(player_name)

    json_pkg = pkg.to_json()
    # Send serialized game state back to client
    emit('game_update', json_pkg)

@socketio.on('updatePlayerOrders')
def handle_orders(data):
    game_id = data['game_id']
    player_name = data['player_name']
    orders = data['orders']

    if game_id in games:
        for player in games[game_id].players:
            if player.name == player_name:
                player.pendingOrders = orders
                break

if __name__ == '__main__':
    socketio.run(app, debug=True)