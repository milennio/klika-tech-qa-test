from math import ceil

from locators import MainPageLocators
from selenium.webdriver.common.by import By

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def examples(self, digit1, action, digit2):
        print(digit1 + ' ' + action + ' ' + digit2)
        for d in digit1:
            if d == "0":
                self.click_digit_zero()
            if d == "1":
                self.click_digit_one()
            if d == "2":
                self.click_digit_two()
            if d == "3":
                self.click_digit_three()
            if d == "4":
                self.click_digit_four()
            if d == "5":
                self.click_digit_five()
            if d == "6":
                self.click_digit_six()
            if d == "7":
                self.click_digit_seven()
            if d == "8":
                self.click_digit_eight()
            if d == "9":
                self.click_digit_nine()
            if d == ".":
                self.click_point()
            else:
                pass

        if action == "+":
            self.click_operation_plus()
        if action == "-":
            self.click_operation_minus()
        if action == "/":
            self.click_operation_sub()
        if action == "*":
            self.click_operation_mult()

        for d in digit2:
            if d == "0":
                self.click_digit_zero()
            if d == "1":
                self.click_digit_one()
            if d == "2":
                self.click_digit_two()
            if d == "3":
                self.click_digit_three()
            if d == "4":
                self.click_digit_four()
            if d == "5":
                self.click_digit_five()
            if d == "6":
                self.click_digit_six()
            if d == "7":
                self.click_digit_seven()
            if d == "8":
                self.click_digit_eight()
            if d == "9":
                self.click_digit_nine()
            if d == ".":
                self.click_point()
            else:
                pass

        self.click_operation_equals()

    def example_with_multiple_actions(self, action, digit2):
        if action == "+":
            self.click_operation_plus()
        if action == "-":
            self.click_operation_minus()
        if action == "/":
            self.click_operation_sub()
        if action == "*":
            self.click_operation_mult()

        for d in digit2:
            if d == "0":
                self.click_digit_zero()
            if d == "1":
                self.click_digit_one()
            if d == "2":
                self.click_digit_two()
            if d == "3":
                self.click_digit_three()
            if d == "4":
                self.click_digit_four()
            if d == "5":
                self.click_digit_five()
            if d == "6":
                self.click_digit_six()
            if d == "7":
                self.click_digit_seven()
            if d == "8":
                self.click_digit_eight()
            if d == "9":
                self.click_digit_nine()
            if d == ".":
                self.click_point()
            else:
                pass

        self.click_operation_equals()


    def is_title_matches(self):
        """Verifies that the hardcoded text "Calculator" appears in page title"""
        return "Calculator" in self.driver.title

    def is_result_matching_display(self):
        """Verifies """
        result = self.driver.find_element(By.ID, 'display').text
        print('The result is ' + result)
        return float(result)

    def click_point(self):
        """Clicks "." digit"""
        element = self.driver.find_element(*MainPageLocators.POINT_DIGIT)
        element.click()

    def click_digit_zero(self):
        """Clicks "0" digit"""
        element = self.driver.find_element(*MainPageLocators.ZERO_DIGIT)
        element.click()

    def click_digit_one(self):
        """Clicks "1" digit"""
        element = self.driver.find_element(*MainPageLocators.ONE_DIGIT)
        element.click()

    def click_digit_two(self):
        """Clicks "2" digit"""
        element = self.driver.find_element(*MainPageLocators.TWO_DIGIT)
        element.click()

    def click_digit_three(self):
        """Clicks "3" digit"""
        element = self.driver.find_element(*MainPageLocators.THREE_DIGIT)
        element.click()

    def click_digit_four(self):
        """Clicks "4" digit"""
        element = self.driver.find_element(*MainPageLocators.FOUR_DIGIT)
        element.click()

    def click_digit_five(self):
        """Clicks "5" digit"""
        element = self.driver.find_element(*MainPageLocators.FIVE_DIGIT)
        element.click()

    def click_digit_six(self):
        """Clicks "6" digit"""
        element = self.driver.find_element(*MainPageLocators.SIX_DIGIT)
        element.click()

    def click_digit_seven(self):
        """Clicks "7" digit"""
        element = self.driver.find_element(*MainPageLocators.SEVEN_DIGIT)
        element.click()

    def click_digit_eight(self):
        """Clicks "8" digit"""
        element = self.driver.find_element(*MainPageLocators.EIGHT_DIGIT)
        element.click()

    def click_digit_nine(self):
        """Clicks "9" digit"""
        element = self.driver.find_element(*MainPageLocators.NINE_DIGIT)
        element.click()

    def click_operation_plus(self):
        """Clicks "+" button"""
        element = self.driver.find_element(*MainPageLocators.PLUS_OPERATION)
        element.click()

    def click_operation_minus(self):
        """Clicks "-" button"""
        element = self.driver.find_element(*MainPageLocators.MINUS_OPERATION)
        element.click()

    def click_operation_mult(self):
        """Clicks "*" button"""
        element = self.driver.find_element(*MainPageLocators.MULT_OPERATION)
        element.click()

    def click_operation_sub(self):
        """Clicks "/" button"""
        element = self.driver.find_element(*MainPageLocators.SUB_OPERATION)
        element.click()

    def click_operation_equals(self):
        """Clicks "=" button"""
        element = self.driver.find_element(*MainPageLocators.EQUALS_OPERATION)
        element.click()

    def click_operation_clear(self):
        """Clicks "C" button"""
        element = self.driver.find_element(*MainPageLocators.CLEAR_OPERATION)
        element.click()

    def click_operation_all_clear(self):
        """Clicks "AC" button"""
        element = self.driver.find_element(*MainPageLocators.ALL_CLEAR_OPERATION)
        element.click()
