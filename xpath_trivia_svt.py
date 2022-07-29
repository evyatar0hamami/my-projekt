import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import string
import time
import unittest
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def driver():
    driver = webdriver.Chrome("/Users/evyatarhamami/Desktop/selenium/chromedriver")
    driver.get("https://shemsvcollege.github.io/Trivia/")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3)
    yield driver
    time.sleep(2)
    driver.quit()


def find_element_by_xpath(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='text'])[1]")


class Question:
    def __init__(self,hp_strar_button, question, answer_1, answer_2, answer_3, answer_4):
        self.hp_strar_button = hp_strar_button
        self.hp_strar_button = (By.ID, "startB")
        self.question = question
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4


    def xpath_q1_first_question_text(self):
        return driver.find_element_by_xpath("(//INPUT[@type='text'])[1]")





# class Question:
#     def __init__(self, question, answer_1, answer_2, answer_3, answer_4, xpath_first_question,
#                  xpath_second_question, xpath_third_question, xpath_fourth_question, xpath_first_question_button,
#                  xpath_second_question_button, xpath_third_question_button, xpath_fourth_question_button):
#         self.question = question
#         self.answer_1 = answer_1
#         self.answer_2 = answer_2
#         self.answer_3 = answer_3
#         self.answer_4 = answer_4
#
#
# class Xpath:
#     def __init__(self, xpath_second_question, xpath_third_question, xpath_fourth_question, xpath_first_question_button,
#                  xpath_second_question_button, xpath_third_question_button, xpath_fourth_question_button):
#         self.xpath_second_question = xpath_second_question
#         self.xpath_third_question = xpath_third_question
#         self.xpath_fourth_question = xpath_fourth_question
#         self.xpath_first_question_button = xpath_first_question_button
#         self.xpath_second_question_button = xpath_second_question_button
#         self.xpath_third_question_button = xpath_third_question_button
#         self.xpath_fourth_question_button = xpath_fourth_question_button

def hp_strar_button(driver):
    return driver.find_element(By.ID, "startB")


'''q1 = question no 1 '''


# def xpath_q1_first_question_text(driver):
#     return driver.find_element_by_xpath("(//INPUT[@type='text'])[1]")


def q1_next_button_to_answers(driver):
    return driver.find_element_by_xpath("//BUTTON[@id='nextquest']")


def q1_first_answer_text(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='text'])[2]")


def q1_second_answer_text(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='text'])[3]")


def q1_third_answer_text(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='text'])[4]")


def q1_fourth_answer_text(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='text'])[5]")


def q1_first_radio_button(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='radio'])[1]")

def q1_second_radio_button(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='radio'])[2]")


def q1_third_radio_button(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='radio'])[3]")


def q1_fourth_radio_button(driver):
    return driver.find_element_by_xpath("(//INPUT[@type='radio'])[4]")


def q1_next_button_to_q2(driver):
    return driver.find_element_by_xpath("//BUTTON[@id='nextquest']")


def q1_bake_button(driver):
    return driver.find_element_by_xpath("//BUTTON[@id='backquest']")