import time
from selenium import webdriver
import pytest
from PageObject import HomePage, ContactsPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver


def test1(driver):          #Проверка корректности определения региона
    driver.get("https://sbis.ru/")
    driver.implicitly_wait(10)
    sbis_home = HomePage(driver)
    sbis_contacts = ContactsPage(driver)
    #####################################
    sbis_home.click_contacts()
    assert sbis_contacts.find_region().text == 'Нижегородская обл.' and sbis_contacts.find_city().text == 'Нижний Новгород'


def test2(driver):          #Проверка коррктности поведения при изменении региона
    driver.get("https://sbis.ru/")
    driver.implicitly_wait(10)
    sbis_home = HomePage(driver)
    sbis_contacts = ContactsPage(driver)
    #####################################
    sbis_home.click_contacts()
    sbis_contacts.find_region().click()
    sbis_contacts.click_kamchatka_in_list()
    time.sleep(2)
    assert (sbis_contacts.find_region().text == 'Камчатский край' and sbis_contacts.find_city().text == 'Петропавловск-Камчатский' and
            '41-kamchatskij-kraj' in driver.current_url and 'Камчатский край' in driver.title)