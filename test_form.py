import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestForm:
    def setup_method(self):
        """Setup: open Chrome browser"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(900, 900)
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
        """Teardown: close browser"""
        self.driver.quit()

    def test_form(self):
        """Main test"""
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")

        # Fill out form fields
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("soumya kiran puppala")
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("8555091586")
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("soumyakiranpuppala@gmail.com")
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Venkateswara Colony\nଭେଙ୍କଟେଶ୍ୱର କଲୋନି")
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("761200")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("1992-07-12")
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys("female")
        self.driver.find_element(By.XPATH, "//div[7]/div/div/div[2]/div/div").click()
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[6]").send_keys("GNFPYC")

        # Screenshot before submit
        time.sleep(2)
        self.driver.save_screenshot("form_filled.png")

        # Wait for and click Submit
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Submit')]/ancestor::div[@role='button']"))
        )
        submit_btn.click()

        # Wait for confirmation
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'response has been recorded')]")))

        # Screenshot after submit
        self.driver.save_screenshot("form_submitted.png")
