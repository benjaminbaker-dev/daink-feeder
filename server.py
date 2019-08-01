import os
from flask import Flask, render_template, send_file

import consts

app = Flask(__name__)


@app.route("/meme/<string:meme_id>")
def send_meme(meme_id):
    return send_file(os.path.join(consts.MEME_FOLDER, meme_id))


@app.route("/")
def home():
    return render_template("index.html", meme_id="ckp8ai")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
