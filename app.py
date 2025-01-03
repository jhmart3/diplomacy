from flask import Flask, request, jsonify, render_template
from engine import GameState, create_gameState, checkOptionsOneUnit, Move, Support, processTurns

app = Flask(__name__)

# Store game states in memory
games = {}

# Serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# Game API endpoints
@app.route('/api/game/new', methods=['POST'])
def new_game():
    game_id = len(games)
    games[game_id] = create_gameState()
    return jsonify({
        'game_id': game_id,
        'message': 'New game created'
    })

@app.route('/api/game/<int:game_id>/state')
def get_game_state(game_id):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game = games[game_id]
    state = {
        'nations': [
            {
                'name': nation.name,
                'units': [
                    {
                        'location': unit.location,
                        'type': unit.getType()
                    } for unit in nation.units
                ]
            } for nation in game.nations
        ]
    }
    return jsonify(state)

@app.route('/api/game/<int:game_id>/options/<string:nation_name>')
def get_options(game_id, nation_name):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game = games[game_id]
    nation = next((n for n in game.nations if n.name == nation_name), None)
    
    if not nation:
        return jsonify({'error': 'Nation not found'}), 404
    
    options = {}
    for unit in nation.units:
        unit_options = checkOptionsOneUnit(game, unit)
        moves = []
        supports = []
        
        for option in unit_options:
            if hasattr(option, 'isHold'):
                moves.append({
                    'type': 'move',
                    'target': option.targetProvince,
                    'isHold': option.isHold
                })
            else:
                supports.append({
                    'type': 'support',
                    'supported_unit': {
                        'location': option.supported_move.unit.location,
                        'type': option.supported_move.unit.getType()
                    },
                    'target': option.supported_move.targetProvince
                })
        
        options[unit.location] = {
            'moves': moves,
            'supports': supports
        }
    
    return jsonify(options)

@app.route('/api/game/<int:game_id>/submit-orders', methods=['POST'])
def submit_orders(game_id):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game = games[game_id]
    orders_data = request.json
    
    if not orders_data or 'nation' not in orders_data or 'orders' not in orders_data:
        return jsonify({'error': 'Invalid order format'}), 400
    
    nation = next((n for n in game.nations if n.name == orders_data['nation']), None)
    if not nation:
        return jsonify({'error': 'Nation not found'}), 404
    
    # Convert orders into Move and Support objects
    processed_orders = []
    for unit_loc, order in orders_data['orders'].items():
        unit = next((u for u in nation.units if u.location == unit_loc), None)
        if unit:
            if order['type'] == 'move':
                move = Move(unit, order['target'])
                processed_orders.append(move)
            elif order['type'] == 'support':
                for n in game.nations:
                    supported_unit = next((u for u in n.units if u.location == order['supported_unit']['location']), None)
                    if supported_unit:
                        supported_move = Move(supported_unit, order['target'])
                        support = Support(unit, supported_move)
                        processed_orders.append(support)
                        break
    
    # Process orders and get outcomes
    old_state = {nation.name: [(u.location, u.getType()) for u in nation.units] for nation in game.nations}
    game, outcomes = processTurns(game, processed_orders)
    new_state = {nation.name: [(u.location, u.getType()) for u in nation.units] for nation in game.nations}
    
    return jsonify({
        'message': f'Orders processed for {nation.name}',
        'oldState': old_state,
        'newState': new_state,
        'orders': orders_data['orders'],
        'outcomes': outcomes
    })

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)