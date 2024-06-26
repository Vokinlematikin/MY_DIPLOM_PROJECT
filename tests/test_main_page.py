import time
import allure
import pytest_check as check
from locators.locators_main_page import MainPage


@allure.story('Тест для проверки главной страницы сайта')
@allure.feature('Тест для проверки меню Header')
def test_header_menu(web_browser):
    """Этот тест проверяет меню header главной страницы сайта"""

    page = MainPage(web_browser)

    elements_headers = [
        (page.btn_header_series, 'СЕРИАЛЫ'),
        (page.btn_header_movies, 'КИНО'),
        (page.btn_header_news, 'НОВОСТИ'),
        (page.btn_header_video, 'ВИДЕО'),
        (page.btn_header_new, 'НОВИНКИ'),
        (page.btn_header_schedule, 'РАСПИСАНИЕ')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы сайта')
@allure.feature('Тест для проверки меню footer')
def test_footer_menu(web_browser):
    """Этот тест проверяет меню footer главной страницы сайта"""

    page = MainPage(web_browser)

    elements_footers = [
        (page.btn_footer_series, 'Сериалы'),
        (page.btn_footer_news, 'Новости'),
        (page.btn_footer_new, 'Новинки'),
        (page.btn_footer_video, 'Видео'),
        (page.btn_footer_schedule, 'Расписание'),
        (page.btn_footer_official, 'Официальная группа в VK'),
        (page.btn_footer_about, 'О проекте'),
        (page.btn_footer_rules, 'Правила'),
        (page.btn_footer_faq, 'FAQ'),
        (page.btn_footer_reklama, 'Размещение рекламы'),
        (page.btn_footer_feedback, 'Обратная связь'),
        (page.btn_footer_rss, 'RSS')
    ]

    for elements, elements_text in elements_footers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки формы поиска')
@allure.feature('Тест для проверки и отображения формы поиска на главной странице')
def test_header_search(web_browser):
    """Этот тест проверяет форму отображения поиска на главной страницы сайта"""

    page = MainPage(web_browser)

    with allure.step('Проверка на отображение'):
        check.is_true(page.header_search_input.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.header_search_input.is_clickable())

    with allure.step('Проверка placeholder поиска'):
        check.equal(page.header_search_input.get_attribute('placeholder'), 'Поиск')


@allure.story('Тест для проверки формы поиска элементов на сайте')
@allure.feature('Тест для поиска нескольких элементов на сайте')
def test_header_search_results(web_browser):
    """Этот тест проверяет форму поиска на главной страницы сайта.
     В результате поиска по запросу должны появится минимум 2 блока"""

    page = MainPage(web_browser)
    time.sleep(1)

    search_words = 'во все тяжкие'
    time.sleep(1)

    page.header_search_input.send_keys(search_words)

    page.header_search_btn.click()
    time.sleep(1)

    with allure.step(f'Проверка, что поиск выдал страницу с результатами поиска'):
        check.is_true(page.result_search_list.is_visible())

    with allure.step(f'Проверка, что результатов выдачи поиска больше одного'):
        check.greater_equal(page.result_search_row.count(), 2)

    count = 1
    for article in page.result_search_row:
        with allure.step(f'Проверка, что блок выдачи № {count} содержит ключевой запрос "{search_words}"'):
            check.is_true(article.text.find(search_words))
        count += 1


@allure.story('Тест для проверки формы поиска элемента на сайте')
@allure.feature('Тест для поиска одного элемента на сайте')
def test_header_search_result(web_browser):
    """Этот тест проверяет форму поиска на главной страницы сайта.
     В результате поиска по запросу должен появится только один блок"""

    page = MainPage(web_browser)

    time.sleep(2)

    search_words = 'el camino'

    page.header_search_input.send_keys(search_words)

    page.header_search_btn.click()
    time.sleep(2)

    with allure.step(f'Проверка, что поиск выдал страницу с результатами поиска'):
        check.is_true(page.result_search_list.is_visible())

    with allure.step(f'Проверка, что результатов поиска больше одного'):
        check.greater_equal(page.result_search_row.count(), 1)

    count = 1
    for article in page.result_search_row:
        with allure.step(f'Проверка, что статья № {count} содержит искомое слово "{search_words}"'):
            check.is_true(article.text.find(search_words))
        count += 1


@allure.story('Тест проверки ссылок')
@allure.feature('Тест для проверки адреса ссылки логин')
def test_link_login(web_browser):
    """Этот тест проверяет адрес ссылок в кнопках """

    page = MainPage(web_browser)

    with allure.step('Проверка на отображение и кликабельность'):
        check.is_true(page.btn_link_login.is_clickable())
        check.is_true(page.btn_link_login.is_visible())
        check.equal(page.btn_link_login.get_attribute('href'), 'https://www.lostfilm.tv/login')


@allure.story('Тест проверки ссылок')
@allure.feature('Тест для проверки адреса ссылки регистрации')
def test_link_reg(web_browser):
    """Этот тест проверяет адрес ссылок в кнопках """

    page = MainPage(web_browser)

    with allure.step('Проверка на отображение и кликабельность'):
        check.is_true(page.btn_link_reg.is_clickable())
        check.is_true(page.btn_link_reg.is_visible())
        check.equal(page.btn_link_reg.get_attribute('href'), 'https://www.lostfilm.tv/reg')
