
import time
from pages.homepage import HomePage
from pages.product import ProductPage



#поиск заголовка по елементу с помощью паф запроса
def test_open_s6(browser):

    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

#проверка что на странице 2 товара
def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get('https://demoblaze.com/index.html')
    homepage.click_monitor()
    #monitor_link = browser.find_element(By.CSS_SELECTOR, '''[oneclick="buCat('monitor')"]''' )
    #monitor_link.click()
    time.sleep(2) #НЕ ИСПОЛЬЗОВАТЬ В АВТОТЕСТАХ
    homepage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR,'.card' )
    #assert len(monitors) == 2  #с помощью len узнаем кол-во в списке monitors и проверяю, что их 2