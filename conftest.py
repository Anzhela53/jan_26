from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options) # Инициализация драйвера
    browser.maximize_window()
    browser.implicitly_wait(3) # включаем неявное ожидание в течении 3 секунд после загрузки страницы( неявное одидание ждет пока на странице появится элементы которые ищем
    yield browser
    browser.close()