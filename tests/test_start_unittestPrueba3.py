import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_find_h1(self):
        self.driver.get("https://leofabro.github.io/PaginaPruebas/")
        # Esperar hasta que el elemento <h1> esté presente
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertIsNotNone(element)

    def test_find_paragraph(self):
        self.driver.get("https://leofabro.github.io/PaginaPruebas/")
        # Esperar hasta que el elemento <p> esté presente
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )
        self.assertIsNotNone(element)

if __name__ == "__main__":
    unittest.main()
