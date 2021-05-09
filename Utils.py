import os


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def del_scores_file():
    if os.path.exists("Scores.txt"):
        os.remove("Scores.txt")
