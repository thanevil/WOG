from exchangeratesapi import Api
from random import randint


# get exchange rate from ILS to USD
def exchange_rate():
    api = Api()
    ils_usd = api.get_rate('USD', 'ILS')
    formatted_rate = round(ils_usd, 1)  # "{:.2f}".format(ils_usd)
    return formatted_rate


# generates a random number between 1 - 10 and multiplies by exchange rate
def get_money_interval(difficulty, guess, number):
    rate = exchange_rate()
    total = rate * number
    if int(total) - (5 - int(difficulty)) < int(guess) < int(total) + (5 - int(difficulty)):
        print("you guessed right")
        return True
    else:
        print("you might have more luck next time")
        return False


def get_guess_from_user(number):
    guess = input(f'guess how many ILS is {number} in USD (rounded to one decimal): ')
    return guess


# play game
def play_roulette(difficulty):
    print('welcome to the Currency roulette')
    number = randint(1, 100)
    get_money_interval(difficulty, get_guess_from_user(number), number)
