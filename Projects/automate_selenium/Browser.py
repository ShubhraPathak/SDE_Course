from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# === SRP: BrowserDriver handles browser init only ===
class BrowserDriver:
    def __init__(self, headless=True):
        self.headless = headless

    def get_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver


# === SRP: WebActions encapsulates all interactions ===
class WebActions:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, by, value, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        ).click()

    def enter_text(self, by, value, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        ).send_keys(text)

    def get_title(self):
        return self.driver.title

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)


# === OCP: AutomationFlow can be extended for different flows ===
class AutomationFlow:
    def __init__(self, actions: WebActions):
        self.actions = actions

    def run(self, url):
        self.actions.open_url(url)
        print("Title:", self.actions.get_title())

        # Example: Search something
        self.actions.enter_text(By.NAME, "q", "data classes")
        self.actions.click_element(By.ID, "submit")
        self.actions.take_screenshot("search_results.png")
    # AutomationFLow can further be devided into mutiple methods
    # Let's provide some placeholder methods
    
    def search_element_by_name(self):
        pass
    def search_element_by_ID(self):
        pass
    def click_element(self):
        pass
    def is_active(self):
        pass
    def input_text(self):
        pass
    def delete_text(self):
        pass
    def take_page_screenshot(self):
        pass


# === Main Execution ===
if __name__ == "__main__":
    browser = BrowserDriver(headless=True)
    driver = browser.get_driver()
    url = "https://www.python.org"

    try:
        actions = WebActions(driver)
        flow = AutomationFlow(actions)
        flow.run(url)
    finally:
        driver.quit()
