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

@socketio.on('join_game')
def join_game(data):
    game_id = data['game_id']
    player_name = data['player_name']
    
    if game_id not in games:
        player = Player(player_name, "Austria")
        games[game_id] = Game(create_gameState(), [player])
        print(f"Making new game with id {game_id}")

    pkg = games[game_id].getPackage(player_name)

    json_pkg = pkg.to_json()

    emit('game_update', json_pkg)

@socketio.on('manual_turn')
def manualTurn(data):
    game_id = data['game_id']
    player_name = data['player_name']
    games[game_id].processCurrentTurn()


    emit('game_update', json_pkg)
    
@socketio.on('get_game')
def get_game(data):
    game_id = data['game_id']
    player_name = data['player_name']

    pkg = games[game_id].getPackage(player_name)

    json_pkg = pkg.to_json()

    emit('game_update', json_pkg)

@socketio.on('order_update')
def order_update(data):
    game_id = data['game_id']
    player_name = data['player_name']
    raw_orders = data['orders']
    
    orders = convert_orders_from_json(raw_orders)

    print("Received orders")
    if game_id in games:
        for player in games[game_id].players:
            if player.name == player_name:
                player.pendingOrders = orders
                print(f"Orders for {player.name} ({player.nation_str}) updated")
                #print(orders)
                break

    pkg = games[game_id].getPackage(player_name)

    json_pkg = pkg.to_json()

    emit('game_update', json_pkg)
    

if __name__ == '__main__':
    socketio.run(app, debug=True)