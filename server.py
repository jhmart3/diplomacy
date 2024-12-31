from flask import Flask, request, jsonify
from flask_cors import CORS
from jmbackend import create_gameState, getAllMoves 

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend access

game_state = create_gameState()  # Initialize game state

@app.route("/game_state", methods=["GET"])
def game_state_endpoint():
    """Endpoint to get the current game state."""
    return jsonify(send_game_state(game_state))

@app.route("/potential_orders", methods=["POST"])
def potential_orders_endpoint():
    """Endpoint to get potential orders for a specific nation."""
    data = request.json
    nation_name = data.get("nation")
    
    if not nation_name:
        return jsonify({"error": "Nation name is required."}), 400

    nation = next((n for n in game_state.nations if n.name == nation_name), None)
    if not nation:
        return jsonify({"error": f"Nation '{nation_name}' not found."}), 404

    orders = getAllMoves(game_state)
    return jsonify(orders)

@app.route("/final_orders", methods=["POST"])
def final_orders_endpoint():
    """Endpoint to submit final orders."""
    data = request.json
    orders = data.get("orders")

    if not orders:
        return jsonify({"error": "Orders data is required."}), 400

    try:
        results = process_final_orders(game_state, orders)
        newspaper = send_newspaper(results)
        return jsonify(newspaper)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def serve_index():
    """Serve the index.html file."""
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
