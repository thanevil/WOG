import os


# cleans the CLI screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


# test to ensure score is calculated correctly
def calc_score():
    score = open("Scores.txt", "r")
    for line in score:
        print(line)
