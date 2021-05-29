from flask import Flask, render_template
from mysql.connector import connect

app = Flask(__name__)


@app.route('/score')
def score_server():
    try:
        conn = connect(host="mysqldb", user="root", password="password", database="games", autocommit=True)
        cursor = conn.cursor()
        cursor.execute("SELECT score FROM users_scores WHERE ID = '1'")
        record = cursor.fetchone()
        score = int(record[0])
        return render_template('index.html', SCORE=score)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8777)
