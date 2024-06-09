import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_button_add_to_basket(browser: WebDriver):
    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) == 1, "Кнопки нет"
