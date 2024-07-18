from selenium import webdriver
import pytest
from PageObject import HomePage, ContactsPage, TensorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver


def test1(driver):          #Проверка наличия блока "Сила в людях"
    driver.get("https://sbis.ru/")
    driver.implicitly_wait(10)
    sbis_home = HomePage(driver)
    sbis_contacts = ContactsPage(driver)
    tensor = TensorPage(driver)
    #####################################
    sbis_home.click_contacts()
    sbis_contacts.click_banner()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    assert tensor.find_power_block().is_displayed()


def test2(driver):          #Проверка открытия tensor.ru/about
    driver.get("https://tensor.ru/")
    driver.implicitly_wait(10)
    tensor = TensorPage(driver)
    #####################################
    tensor.scroll_to_news_block(driver)
    tensor.click_more_details()
    assert driver.current_url == 'https://tensor.ru/about'


def test3(driver):          #Проверка высоты и ширины изображений
    driver.get("https://tensor.ru/about")
    driver.implicitly_wait(10)
    tensor = TensorPage(driver)
    assert ((tensor.get_attribute_image(1, 'height') == tensor.get_attribute_image(2, 'height') ==
            tensor.get_attribute_image(3, 'height') == tensor.get_attribute_image(4, 'height')) and
            (tensor.get_attribute_image(1, 'width') == tensor.get_attribute_image(2, 'width') ==
            tensor.get_attribute_image(3, 'width') == tensor.get_attribute_image(4, 'width')))
