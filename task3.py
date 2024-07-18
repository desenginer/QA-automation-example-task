import time
from PageObject import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import re


def wait_for_download(directory, filename, timeout=60):
    """
    Ожидает загрузки файла в указанную директорию.

    directory: Путь к директории для загрузок.
    filename: Имя ожидаемого файла.
    timeout: Время ожидания в секундах.
    True, если файл загружен, иначе False.
    """
    start_time = time.time()
    while True:
        if filename in os.listdir(directory):
            return True
        elif time.time() - start_time > timeout:
            return False
        time.sleep(1)


@pytest.fixture()
def driver():
    current_dir = os.path.dirname(os.path.abspath(__file__))            #Определяем путь для загрузки (папка исполняемого файла)
    download_dir = os.path.join(os.getcwd(), current_dir)
    chrome_options = webdriver.ChromeOptions()                          #Настрока браузера (скачивание файлов без подтверждения, задаём папку для скачивания файлов)
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    return driver


def test1(driver):          #Проверка скачивания файла
    driver.get("https://sbis.ru/")
    driver.implicitly_wait(10)
    sbis_home = HomePage(driver)
    sbis_home.click_download_local_version()
    driver.get("https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe")      #КОСТЫЛЬ. при использовании строк ниже - не хочет скачиваться(неизвестное исключение)
    #time.sleep(2)
    #driver.find_element(By.XPATH, '//*[@id="ws-vd2gfky5rqs1721319524047"]/div[1]/div[2]/div[2]/div/a').click()     #"кнопка" для скачивания
    download_dir = os.path.dirname(os.path.abspath(__file__))
    assert wait_for_download(download_dir, 'sbisplugin-setup-web.exe')              #Спорное решение с явным указанием имени файла, но если до этого он не был загружен
                                                                                            #в директорию с исполняемым файлом, то всё сработает. P.S. Если файл уже был загружен,
                                                                                            #при скачивании к его имени прибавляется "(1)"
def test2(driver):          #Сравнение размера скаченного файла с заявленным
    driver.get("https://sbis.ru/")
    driver.implicitly_wait(10)
    sbis_home = HomePage(driver)
    sbis_home.click_download_local_version()
    #driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a').click()
    #time.sleep(120)
    downland_str = driver.find_element(By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink').text
    site_size = re.findall(r'\d*\.\d+|\d+', downland_str)
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_size = os.path.getsize(file_path + '\\sbisplugin-setup-web.exe')
    file_size = round((file_size/1024)/1024, 2)
    assert float(site_size[0]) == file_size