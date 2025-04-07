import time

matches = {}  # in-memory match store

def create_match(player1, player2, problem, duration):
    match_id = f"{player1}_{player2}_{int(time.time())}"
    matches[match_id] = {
        "players": [player1, player2],
        "problem": problem,
        "start_time": int(time.time()),
        "duration": duration,
        "winner": None
    }
    return match_id

def check_match_status(match_id, utils):
    match = matches.get(match_id)
    if not match or match['winner']:
        return match

    now = int(time.time())
    if now - match['start_time'] > match['duration']:
        match['winner'] = "Draw"
        return match

    contest_id, index = match['problem']
    for player in match['players']:
        submissions = utils.get_recent_submissions(player, contest_id, index, match['start_time'])
        for sub in submissions:
            if sub['verdict'] == 'OK':
                match['winner'] = player
                return match

    return match
