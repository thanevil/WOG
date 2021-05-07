import os


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_scores_file():
    score_file = open("Scores.txt", "w+")
    score_file.close()


def del_scores_file():
    os.remove("Scores.txt")

