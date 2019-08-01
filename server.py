import os
import json
import random

MEME_FOLDER = r"/Users/benjaminbaker/Desktop/meme dataset"
RANK_JSON = r"/Users/benjaminbaker/Desktop/memeranking.json"

RANK_COUNT_KEY = "rank_count"
DANK_COUNT_KEY = "dank_count"


def is_ranked(file_id):
    with open(RANK_JSON, "r") as f:
        ranked_files = json.load(f)
    return file_id in ranked_files.keys()


def get_unranked_file_name():
    files = os.listdir(MEME_FOLDER)
    file_id = random.choice(files)
    try_counter = 1

    while is_ranked(file_id):
        if try_counter == len(files):
            raise ValueError("no more memes !")

        file_id = random.choice(files)
        try_counter += 1
    return file_id


def update_file_id_counter(file_id, key):
    with open(RANK_JSON, "r") as f:
        ranked_files = json.load(f)

    try:
        ranked_files[file_id][key] += 1
    except KeyError:
        ranked_files[file_id] = {}
        ranked_files[file_id][key] = 1

    with open(RANK_JSON, "w") as f:
        json.dump(ranked_files, f)

