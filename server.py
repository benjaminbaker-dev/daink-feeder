import os
from flask import Flask, request, render_template, send_file

import ranking
import consts

app = Flask(__name__)


@app.route("/meme/<string:meme_id>")
def send_meme(meme_id):
    return send_file(os.path.join(consts.MEME_FOLDER, meme_id))


@app.route("/static/<string:f_path>")
def send_script(f_path):
    return send_file(os.path.join("static", f_path))


@app.route("/")
def home():
    meme_id = ranking.get_file_id()
    return render_template("index.html", meme_id=meme_id)


@app.route("/rank", methods=["POST"])
def handle_ranking():
    data = request.json
    meme_id = data[consts.MEME_ID_KEY]
    dank_flag = data[consts.DANK_FLAG_KEY]

    if dank_flag:
        ranking.update_file_id_counter(meme_id, consts.DANK_COUNT_KEY)
    ranking.update_file_id_counter(meme_id, consts.RANK_COUNT_KEY)

    return {"status": "ok"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
