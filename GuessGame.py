import random


# guess the number game, difficulty between 1 and a difficulty selected
def generate_number(difficulty):
    number = random.randint(1, difficulty)
    return int(number)


def get_guess_from_user(difficulty):
    guess = int(input(f"""I am thinking about a number between 1 and {difficulty},
you have to guess the number in three tries.
guess the number: """))
    return int(guess)


def compare_results(guess, number):
    tries = 0
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
        return True
    else:
        print("you lost this game")
        return False


def play_guess(difficulty):
    print("Welcome to the Memory Game")
    compare_results(get_guess_from_user(difficulty), generate_number(difficulty))
