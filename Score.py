import os


# each win adds 1 to the scores file
def add_score(difficulty):
    if os.path.exists(
            '//wsl$/docker-desktop-data/version-pack-data/community/docker/volumes/score-data/_data/Scores.txt'):
        score = open(
            '//wsl$/docker-desktop-data/version-pack-data/community/docker/volumes/score-data/_data/Scores.txt', "r+")
        for num in score:
            score.read()
            new_score = difficulty * 3 + 5 + int(num)
            score.seek(0)
            score.write(str(new_score))
            score.truncate()
    else:
        score = open(
            '//wsl$/docker-desktop-data/version-pack-data/community/docker/volumes/score-data/_data/Scores.txt', "a")
        score.write(str(int(difficulty) * 3 + 5))
        score.close()
