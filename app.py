from flask import Flask, request, jsonify, render_template
import time
import utils
import match_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/start_match', methods=['POST'])
def start_match():
    data = request.get_json()
    player1 = data['player1']
    player2 = data['player2']
    rating = data.get('rating', 1200)
    duration = data.get('duration', 600)

    # Validate handles
    # info = utils.get_user_info([player1, player2])
    # if info['status'] != 'OK':
    #     return jsonify({"error": "Invalid handles"}), 400

    # Select problem
    problem = utils.get_unsolved_random_problem(rating, [player1, player2])
    if not problem:
        return jsonify({"error": "No unsolved problems found"}), 404

    match_id = match_manager.create_match(player1, player2, problem, duration)
    return jsonify({
        "match_id": match_id,
        "problem": {
            "url": f"https://codeforces.com/contest/{problem[0]}/problem/{problem[1]}"
        },
        "start_time": int(time.time())
    })

@app.route('/check_match', methods=['GET'])
def check_match():
    match_id = request.args.get('match_id')
    match = match_manager.check_match_status(match_id, utils)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    return jsonify(match)

if __name__ == '__main__':
    app.run(debug=True)
