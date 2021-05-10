from string import ascii_letters
from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRouletteGame import play_roulette
from Utils import del_scores_file


# name input, verify it is valid name (only letters and more than 2 characters) and print with welcome
def welcome(name):
    del_scores_file()
    while not all(letter in ascii_letters for letter in name) or not name.strip() or not len(name) > 1:
        name = input("are you from earth? please input your name: ").strip().title()

    return (f"Hello {name} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.")


# loop that prints games options, calls game+difficulty selection until user doesnt want to play
def load_game():
    while load_game:
        print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
       guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
        game = select_game()
        difficulty = select_difficulty()
        play_game(game, difficulty)
        again = input("would you like to play another game? ").lower()
        if again == "yes":
            continue
        elif again == "no":
            print("thank you for playing with us")
            del_scores_file()
            break


# call game, when done, ask to play again
def play_game(game, difficulty):
    if game == 1:
        play_memory(difficulty)
    elif game == 2:
        play_guess(difficulty)
    elif game == 3:
        play_roulette(difficulty)


# selection with return as integer 1-3
def select_game():
    game = input("Choose your game number: ")
    lower = game.lower()
    while select_game:
        try:
            if lower.islower():
                game = input("The games options are 1, 2, or 3, let's try again: ")
        except ValueError:
            continue
        if int(game) in range(1, 4):
            print(f"game {game} was selected")
            return int(game)
        else:
            game = input("The games options are 1, 2, or 3, let's try again: ")
            continue


# selection with return as integer 1-5
def select_difficulty():
    difficulty = input("Please choose game difficulty from 1 to 5: ")
    lower = difficulty.lower()
    while select_difficulty:
        try:
            if lower.islower():
                difficulty = input("The difficulties options are 1 - 5, let's try again: ")
        except ValueError:
            continue
        if int(difficulty) < 1:
            difficulty = int(input("you cant game so easy, only 1 - 5: "))
        elif int(difficulty) == 1:
            print("Difficulty baby was selected")
            return int(difficulty)
        elif int(difficulty) == 2:
            print("Difficulty child was selected")
            return int(difficulty)
        elif int(difficulty) == 3:
            print("Difficulty beginner was selected")
            return int(difficulty)
        elif int(difficulty) == 4:
            print("Difficulty pro was selected")
            return int(difficulty)
        elif int(difficulty) == 5:
            print("Difficulty god was selected")
            return int(difficulty)
        else:
            difficulty = input("The difficulties are 1, 2, 3, 4, or 5: ")
            continue
