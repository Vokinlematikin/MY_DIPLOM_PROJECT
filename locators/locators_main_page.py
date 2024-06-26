import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.lostfilm.tv/'

        super().__init__(web_driver, url)

    # header - кнопки меню
    btn_header_series = WebElement(xpath='//div[@class="menu"]//span[contains(text(),"Сериалы")]')
    btn_header_movies = WebElement(xpath='//div[@class="menu"]//span[contains(text(),"Кино")]')
    btn_header_news = WebElement(xpath='//div[@class="menu"]//span[contains(text(),"Новости")]')
    btn_header_video = WebElement(xpath='//div[@class="menu"]//span[contains(text(),"Видео")]')
    btn_header_new = WebElement(xpath='//div[@class="menu"]//span[contains(text(),"Новинки")]')
    btn_header_schedule = WebElement(xpath='//div[@class="menu"]//span[contains(text(),"Расписание")]')

    # footer - кнопки меню
    btn_footer_series = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Сериалы")]')
    btn_footer_news = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Новости")]')
    btn_footer_new = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Новинки")]')
    btn_footer_video = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Видео")]')
    btn_footer_schedule = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Расписание")]')
    btn_footer_official = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Официальная группа в VK")]')
    btn_footer_about = WebElement(xpath='//div[@class="links"]//a[contains(text(),"О проекте")]')
    btn_footer_rules = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Правила")]')
    btn_footer_faq = WebElement(xpath='//div[@class="links"]//a[contains(text(),"FAQ")]')
    btn_footer_reklama = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Размещение рекламы")]')
    btn_footer_feedback = WebElement(xpath='//div[@class="links"]//a[contains(text(),"Обратная связь")]')
    btn_footer_rss = WebElement(xpath='//div[@class="links"]//a[contains(text(),"RSS")]')

    # header - форма поиска
    header_search_input = WebElement(xpath='//form//*[@name="q"]')
    header_search_btn = WebElement(xpath='//*[@type="submit"]')

    # search - блоки результата поиска
    result_search_list = WebElement(xpath='//*[@id="left-pane"]/div/div')

    result_search_row = ManyWebElements(xpath='//div[@class="row-search"]')

    # header - ссылки
    btn_link_login = WebElement(xpath='(//*[@id="main-rightt-side"]//a)[1]')
    btn_link_reg = WebElement(xpath='//*[@class="link gray-color"]')
