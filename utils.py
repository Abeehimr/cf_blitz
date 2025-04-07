import requests
import random

def get_user_info(handles):
    url = f"https://codeforces.com/api/user.info?handles={';'.join(handles)}"
    return requests.get(url).json()

def get_solved_problems(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    res = requests.get(url).json()
    solved = set()
    for sub in res['result']:
        if sub['verdict'] == 'OK':
            pid = (sub['problem']['contestId'], sub['problem']['index'])
            solved.add(pid)
    return solved

def get_unsolved_random_problem(rating, handles):
    url = "https://codeforces.com/api/problemset.problems"
    all_problems = requests.get(url).json()['result']['problems']

    solved = set()
    for handle in handles:
        solved |= get_solved_problems(handle)

    eligible = [
        (p['contestId'], p['index']) for p in all_problems
        if 'rating' in p and p['rating'] == rating and (p['contestId'], p['index']) not in solved
    ]
    
    return random.choice(eligible) if eligible else None

def get_recent_submissions(handle, contest_id, index, since_ts):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    res = requests.get(url).json()
    relevant = []

    for sub in res['result']:
        if sub['creationTimeSeconds'] < since_ts:
            continue
        p = sub['problem']
        if p['contestId'] == contest_id and p['index'] == index:
            relevant.append(sub)
    
    return relevant
