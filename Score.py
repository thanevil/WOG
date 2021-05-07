# each win adds 1 to the scores file
def add_score():
    score = open("Scores.txt", "a")
    score.write("1")
    score.close()


# test to ensure score is calculated correctly
def calc_score():
    score = open("Scores.txt")
    for line in score.readlines():
        print(int(len(line)) * 3 + 5)
