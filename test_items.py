import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presense_of_add_button(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    time.sleep(10)
    assert True

# не забываем оставить пустую строку в конце файла

