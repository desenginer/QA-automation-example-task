from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.contacts = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a')
        self.download_local_version = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')

    def click_contacts(self):
        self.driver.find_element(*self.contacts).click()

    def click_download_local_version(self):
        self.driver.find_element(*self.download_local_version).click()


class ContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.banner_tensor = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
        self.region = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
        self.city_developer = (By.XPATH, '//*[@id="city-id-2"]')
        self.kamchatka_in_list = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]')

    def click_banner(self):
        self.driver.find_element(*self.banner_tensor).click()

    def find_region(self):
        return self.driver.find_element(*self.region)

    def find_city(self):
        return self.driver.find_element(*self.city_developer)

    def click_kamchatka_in_list(self):
        self.driver.find_element(*self.kamchatka_in_list).click()

class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.power_block = (By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
        self.more_details = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
        self.news_block = (By.XPATH, '//*[@id="container"]/div[1]/div/div[6]/div/div[1]/div')
        self.img1 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')
        self.img2 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img')
        self.img3 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img')
        self.img4 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img')

    def find_power_block(self):
        return self.driver.find_element(*self.power_block)

    def click_more_details(self):
        self.driver.find_element(*self.more_details).click()

    def scroll_to_news_block(self, driver):
        news = self.driver.find_element(*self.news_block)
        actions = ActionChains(driver)
        actions.move_to_element(news).perform()

    def get_attribute_image(self, image_number, attribute):
        match image_number:
            case 1:
                return self.driver.find_element(*self.img1).get_attribute(attribute)
            case 2:
                return self.driver.find_element(*self.img2).get_attribute(attribute)
            case 3:
                return self.driver.find_element(*self.img3).get_attribute(attribute)
            case 4:
                return self.driver.find_element(*self.img4).get_attribute(attribute)
