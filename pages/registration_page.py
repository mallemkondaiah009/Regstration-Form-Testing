from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    address = (By.XPATH, "//textarea[@ng-model='Adress']")
    email = (By.XPATH, "//input[@type='email']")
    phone = (By.XPATH, "//input[@ng-model='Phone']")
    gender_male = (By.XPATH, "//input[@value='Male']")
    hobbies_checkbox3 = (By.XPATH, "//input[@id='checkbox3']")
    languages_dropdown = (By.XPATH, "//div[@id='msdd']")
    languages_list = (By.XPATH, "//li")
    skills = (By.XPATH, "//select[@id='Skills']")
    countries_dropdown = (By.XPATH, "//select[@id='countries']")
    country_option = (By.XPATH, "//b[@role='presentation']")
    country_list = (By.XPATH, "//span//ul//li")
    year = (By.XPATH, "//select[@id='yearbox']")
    month = (By.XPATH, "//select[@placeholder='Month']")
    day = (By.XPATH, "//select[@id='daybox']")
    first_password = (By.XPATH, "//input[@id='firstpassword']")
    second_password = (By.XPATH, "//input[@id='secondpassword']")
    upload_image = (By.XPATH, "//input[@id='imagesrc']")
    submit_button = (By.XPATH, "//button[@id='submitbtn']")

    # Methods for interacting with the elements
    def fill_form(self, first_name, last_name, address, email, phone, image_path):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.phone).send_keys(phone)

    def select_gender(self):
        self.driver.find_element(*self.gender_male).click()

    def select_hobby(self):
        self.driver.find_element(*self.hobbies_checkbox3).click()

    def select_language(self, language):
        self.driver.find_element(*self.languages_dropdown).click()
        languages = self.driver.find_elements(*self.languages_list)
        for lang in languages:
            if lang.text == language:
                lang.click()
                break

    def select_skills(self, skill):
        Select(self.driver.find_element(*self.skills)).select_by_visible_text(skill)

    def select_country(self):
        self.driver.find_element(*self.country_option).click()
        country_list = self.driver.find_elements(*self.country_list)
        for c in country_list:
            if c.text == "India":
                c.click()
                break

    def select_dob(self, year, month, day):
        Select(self.driver.find_element(*self.year)).select_by_visible_text(year)
        Select(self.driver.find_element(*self.month)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.day)).select_by_visible_text(day)

    def set_password(self, password):
        self.driver.find_element(*self.first_password).send_keys(password)
        self.driver.find_element(*self.second_password).send_keys(password)

    def upload_image(self, image_path):
        self.driver.find_element(*self.upload_image).send_keys(image_path)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
