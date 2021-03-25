from live import play_again
import random

# guess the number game, difficulty between 1 and a difficulty selected


def guess_game(difficulty):
    print("Welcome to the Memory Game")
    number = random.randint(1, difficulty)
    tries = 0
    guess = int(input("i am thinking about a number between and b, you have to"
                      "guess the number in three tries"
                      "guess the number: "))
    tries += 1
    if guess > number:
        print("guess lower ;)")
    if guess < number:
        print("guess higher")
    while guess != number and tries < 3:
        guess = int(input("try again: "))
        tries += 1
        if guess > number:
            print("guess lower")
        if guess < number:
            print("guess higher")
    if guess == number:
        print(f"you guessed correctly after {tries} attempts")
    else:
        print("you lost this game")
    play_again()
