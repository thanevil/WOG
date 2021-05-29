from mysql.connector import connect

conn = connect(host="127.0.0.1", user="root", password="password", database="games", autocommit=True)
cursor = conn.cursor()


def add_score(difficulty):
    cursor.execute("SELECT score FROM users_scores WHERE ID = '1'")
    record = cursor.fetchone()
    cursor.execute(
        "UPDATE users_scores SET score = (%s + (%s * 3) + 5) WHERE id = '1';" % (int(record[0]), difficulty))

