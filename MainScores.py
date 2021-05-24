from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/score')
def score_server():
    if os.path.exists("Scores.txt"):
        with open("Scores.txt", "r") as f:
            score = f.read()
            f.close()
            return render_template('index.html', SCORE=score)
    else:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8777)
