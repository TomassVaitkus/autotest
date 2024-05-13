import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


driver = webdriver.Chrome()
URL = "https://demo.betgames.tv"


def exception_function(inp):
    with open("test_results.txt", "a") as f:
        f.write(str(inp))


def test_status():
    try:
        response = requests.get(URL)
        assert response.status_code == 200, "[!!!!!!!!!!!!!! PAGE UNREACHABLE !!!!!!!!!!!!!]"
    except Exception as e:
        exception_function(e)
        raise e


def test_content():
    try:
        response = requests.get(URL)
        assert 'betgames' in response.text, "[THERE'S NO SUCH WORD IN CONTENT]"
    except Exception as e:
        exception_function(e)
        raise e


@pytest.fixture
def browser():
    yield driver
    driver.quit()


def test_language_button_click(browser):
    try:
        browser.get(URL)
        lang_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/ul[1]/li[2]/a")
        ActionChains(browser).click(lang_button).perform()
        '''
        cia uzkomentuota eilute skirta pasitikrinimui ar pagauna klaida ir iraso i faila.
        Ja atkomentavus testas nepraeis nes tokios klases neras ir bus sukurtas klaidos txt failas su irasyta klaida
        '''
        # assert browser.find_element(By.CLASS_NAME, "dropdown-tooggle").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "dropdown-toggle").is_displayed()
    except Exception as e:
        exception_function(e)
        raise e


if __name__ == "__main__":
    pytest.main()

