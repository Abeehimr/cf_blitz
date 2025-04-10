# Codeforces Blitz - 1v1 Match Platform

A lightweight web application for 1v1 blitz-style Codeforces battles. Players compete to solve a random unsolved problem of a given rating. The first player to solve the problem wins the match.

Built with:
- Python (Flask)
- Codeforces API
- HTML + Vanilla JavaScript

---

## Features

- Validates Codeforces handles
- Selects a random problem of the chosen rating that neither player has solved
- Starts a match with a countdown timer
- Tracks submissions live via Codeforces API
- Declares the winner based on the first successful submission

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abeehimr/codeforces_blitz.git
cd codeforces-blitz
