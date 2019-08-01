import os
import json
import random

MEME_FOLDER = r"/Users/benjaminbaker/Desktop/meme dataset"
RANK_JSON = r"/Users/benjaminbaker/Desktop/memeranking.json"

RANK_COUNT_KEY = "rank_count"
DANK_COUNT_KEY = "dank_count"


def _read_rank_json() -> dict:
    try:
        with open(RANK_JSON, "r") as f:
            ranked_files = json.load(f)
        return ranked_files
    except json.JSONDecodeError:
        return {}


def _write_rank_json(rank_json: dict):
    with open(RANK_JSON, "w") as f:
        json.dump(rank_json, f)


def _is_ranked(file_id):
    rank_json = _read_rank_json()
    return file_id in rank_json.keys()


def get_unranked_file_name():
    files = os.listdir(MEME_FOLDER)
    file_id = random.choice(files)
    try_counter = 1

    while _is_ranked(file_id):
        if try_counter == len(files):
            raise ValueError("no more memes !")

        file_id = random.choice(files)
        try_counter += 1
    return file_id


def update_file_id_counter(file_id, key):
    rank_json = _read_rank_json()

    try:
        rank_json[file_id][key] += 1
    except KeyError:
        rank_json[file_id] = {}
        rank_json[file_id][key] = 1

    _write_rank_json(rank_json)
