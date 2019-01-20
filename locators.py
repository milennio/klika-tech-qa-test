from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

        ####OPERATIONS###

    CLEAR_OPERATION = (By.CSS_SELECTOR, '.operations > li:nth-child(1)')
    ALL_CLEAR_OPERATION = (By.CSS_SELECTOR, '.operations > li:nth-child(2)')
    MULT_OPERATION = (By.CSS_SELECTOR, '.operations > li:nth-child(3)')
    SUB_OPERATION = (By.CSS_SELECTOR, '.operations > li:nth-child(4)')
    PLUS_OPERATION = (By.CSS_SELECTOR, '.operations > li:nth-child(5)')
    MINUS_OPERATION = (By.CSS_SELECTOR, '.operations > li:nth-child(6)')
    EQUALS_OPERATION = (By.CSS_SELECTOR, 'li.double:nth-child(7)')

        ###DIGITS###

    SEVEN_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(1)')
    EIGHT_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(2)')
    NINE_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(3)')
    FOUR_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(4)')
    FIVE_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(5)')
    SIX_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(6)')
    ONE_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(7)')
    TWO_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(8)')
    THREE_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(9)')
    ZERO_DIGIT = (By.CSS_SELECTOR, 'li.double:nth-child(10)')
    POINT_DIGIT = (By.CSS_SELECTOR, '.digits > li:nth-child(11)')

    DIGIT_DISPLAYED = (By.ID, 'display')

