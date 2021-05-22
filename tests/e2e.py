from selenium import webdriver
import sys
import os


url = os.getenv("URL")


def test_scores_service():
    # url = input("what is the current url (ex.http://127.0.0.1:5000/score): ")
    driver = webdriver.Chrome()
    driver.get(url)
    score = driver.find_element_by_id("score").text
    if 1 < int(score) < 1000:
        print("test passed!")
        return True
    else:
        print("test failed")
        return False


def main_function():
    try:
        test_scores_service()
    except ValueError:
        sys.exit(-1)


main_function()
