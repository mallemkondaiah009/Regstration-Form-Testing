import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Base.base import BaseTest  # Import the BaseTest class
from pages.registration_page import RegistrationPage
import HtmlTestRunner

class RegistrationTest(BaseTest):

    def test_registration(self):
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Register.html")

        # Instantiate the registration page object
        registration_page = RegistrationPage(driver)

        # Fill in the form using page object methods
        registration_page.fill_form(
            "Mallem", "Kondaiah", "Marlagunta Village, Dakkili Mandal", "smk@gmail.com", "1234567890",
            r"C:\\Users\\Mallem Kondaiah\\OneDrive\\Pictures\\Saved Pictures\\luffy.jpg"
        )
        registration_page.select_gender()
        registration_page.select_hobby()
        registration_page.select_language("Greek")
        registration_page.select_skills("Python")
        registration_page.select_country()
        registration_page.select_dob("2003", "May", "25")
        registration_page.set_password("smk123")
        registration_page.submit_form()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\\Users\\Mallem Kondaiah\OneDrive\\Desktop\\Regstration-Form-Testing\\Reports'),
        verbosity=2,
        argv=['first-arg-is-ignored'],  # Ignore Jupyter notebook arguments
        exit=False  # Prevents the notebook from closing after running the tests
    )
