import os


# each win adds 1 to the scores file
def add_score(difficulty):
    if os.path.exists("Scores.txt"):
        score = open("Scores.txt", "r+")
        for num in score:
            score.read()
            new_score = difficulty * 3 + 5 + int(num)
            score.seek(0)
            score.write(str(new_score))
            score.truncate()
    else:
        score = open("Scores.txt", "a")
        score.write(str(int(difficulty) * 3 + 5))
        score.close()


# test to ensure score is calculated correctly
def calc_score():
    score = open("Scores.txt", "r")
    for line in score:
        print(line)
