import os
import json
import random

import consts


def _read_rank_json() -> dict:
    try:
        with open(consts.RANK_JSON, "r") as f:
            ranked_files = json.load(f)
        return ranked_files
    except json.JSONDecodeError:
        return {}


def _write_rank_json(rank_json: dict):
    with open(consts.RANK_JSON, "w") as f:
        json.dump(rank_json, f)


def get_file_id():
    files = os.listdir(consts.MEME_FOLDER)
    file_id = random.choice(files)
    return file_id


def update_file_id_counter(file_id, key):
    rank_json = _read_rank_json()

    if file_id not in rank_json:
        rank_json[file_id] = {}

    if key not in rank_json[file_id]:
        rank_json[file_id][key] = 1
    else:
        rank_json[file_id][key] += 1

    _write_rank_json(rank_json)
