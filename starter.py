# CS 335 — Introduction to Artificial Intelligence
# API Assignment Starter Code — Northeastern Illinois University
#
# TODO: Replace BASE_URL, endpoints, params, and payload fields
#       with values from your chosen API's documentation.
# ─────────────────────────────────────────────────────────────

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE URL not found. Did you copy .env.example to .env?")

# TODO: Replace with your API's base URL
BASE_URL = os.getenv("BASE_URL")

# update or extend per call if your API requires it
HEADERS = {

    "Content-Type": "application/json",
}


def divider(label):
    print(f"\n{'=' * 50}\n{label}\n{'=' * 50}")


# ── Call 1: GET request ───────────────────────────────────
# Use for retrieving data without a request body.
# TODO: Update url and params.
def call_one_get():
    divider("CALL 1 — GET Pokemon Request")

    url = f"{BASE_URL}/pokemon/jirachi"
    params = {}

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()

        print(f"Name: {data.get('name')}")
        print(f"ID: {data.get('id')}")
        print(f"Weight: {data.get('weight')}")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 2: POST request ──────────────────────────────────
# Use for sending data to the API (e.g., a prompt or input text).
# TODO: Update url and payload fields.
# Hi professor I had to change this and call 3 to another GET request since PokeAPI is read-only
def call_two_post():
    divider("CALL 2 — GET Ability Data")

    url = f"{BASE_URL}/ability/serene-grace"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        effect_entries = data.get('effect_entries', [])
        english_effect = "Description not found"

        for entry in effect_entries:
            if entry.get('language').get('name') == 'en':
                english_effect = entry.get('short_effect')
                break

        print(f"Ability Name: {data.get('name')}")
        print(f"Main Effect: {english_effect}")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 3: Parameterized POST ────────────────────────────
# Same as Call 2 but accepts dynamic input to show varied output.
# TODO: Update url and payload fields.
# Kept the original instructions but the POST call was changed to a GET for call 3

def call_three_get(pokemon_name: str):
    divider(f"CALL 3 - User Search | input: '{pokemon_name}'")

    url = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print(f"Found: {data.get('name')}")
        print(f"ID: {data.get('id')}")
        print(f"Weight: {data.get('weight')}")
    else:
        print(f"[ERROR] Could not find Pokémon: {pokemon_name}")


if __name__ == "__main__":
    call_one_get()
    call_two_post()

    user_choice = input("\nEnter a Pokémon name (in lowercase) to search: ")
    call_three_get(user_choice)
