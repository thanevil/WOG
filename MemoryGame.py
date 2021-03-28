import random
import time
import os


# generate list of numbers (length = difficulty) between 1 and 101
def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    print(random_list)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_list


# creates a list of numbers from user input
def get_list_from_user(difficulty):
    print(f"you need to input the {difficulty} numbers, one at a time")
    user_list = []
    i = 0
    while i < int(difficulty):
        user_input = input("Please input number:")
        user_list.append(int(user_input))
        i = i + 1
    print(user_list)
    return user_list


# verifies the generated and the user input list are equal/not equal
def is_list_equal(guess, generated):
    if guess == generated:
        print("great memory!")
        return True
    else:
        print("you need to work on that memory")
        return False


# run the game
def play_memory(difficulty):
    print(f"""welcome to the Memory Game
    i will display {difficulty} numbers for 0.7 seconds and you will have to remember them in the correct order. 
    get ready!""")
    for x in range(0, 5):  # will display loading for 5 second for the user to prepare
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(1)
    is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))
