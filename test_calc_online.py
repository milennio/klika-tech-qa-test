import unittest

import HtmlTestRunner

from selenium import webdriver
import page

class OnlineCalculatorTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa-test.klika-tech.com/")
        main_page = page.MainPage(self.driver)          #Load the main page
        assert main_page.is_title_matches(), \
            "The title doesn't match."         #Checks if the word "Calculator" is in title

    def test_with_multiple_actions(self):
        main_page = page.MainPage(self.driver)          #Load the main page
        main_page.examples("7", "+", "8")
        assert main_page.is_result_matching_display() == 15, "It's not 15"
        main_page.example_with_multiple_actions("/", "3")
        assert main_page.is_result_matching_display() == 5, "It's not 5"

    def test_division(self):
        main_page = page.MainPage(self.driver)          #Load the main page
        main_page.examples("258", "/", "2")
        assert main_page.is_result_matching_display() == 129, "It's not 129"


    def test_multiplication(self):
        main_page = page.MainPage(self.driver)          #Load the main page
        main_page.examples("9564", "*", "142")
        assert main_page.is_result_matching_display() == 1358088, "It's not 1358088"


    def test_addition(self):
        main_page = page.MainPage(self.driver)          #Load the main page
        main_page.examples("10000732", "+", "268")
        assert main_page.is_result_matching_display() == 10001000, "It's not 10001000"

    def test_subtraction(self):
        main_page = page.MainPage(self.driver)          #Load the main page
        main_page.examples("8", "-", "10")
        assert main_page.is_result_matching_display() == -2, "It's not -2"


    def test_action_with_float_numbers(self):
        main_page = page.MainPage(self.driver)          #Load the main page
        main_page.examples("0.654", "-", "0.004")
        assert main_page.is_result_matching_display() == 0.65, "It's not 0.65"


    def tearDown(self):
        main_page = page.MainPage(self.driver)
        main_page.click_operation_all_clear()
        self.driver.close()

if __name__ == "__main__":
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./html_report'))