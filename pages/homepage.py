from selenium.webdriver.common.by import  By

class HomePage:


    def __init__(self, browser):  #передаем в класс браузер. При передаче сохраняем его в self.browser(обращаясь к странице браузера)
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/index.html') #со страницы берем этот браузер и получаем доступ к той странице, которая нужна



    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text() = "Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count