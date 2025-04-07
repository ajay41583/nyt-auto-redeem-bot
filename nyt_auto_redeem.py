from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("user-data-dir=C:/Users/apatel/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Default")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.dppl.org/resources/subjects/paywall-free-newspapers")
    time.sleep(3)

    links = driver.find_elements(By.PARTIAL_LINK_TEXT, "New York Times")
    if len(links) >= 2:
        links[1].click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])

        # Wait for "Redeem" button to appear and click it
        wait = WebDriverWait(driver, 10)
        redeem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='btn-redeem']")))
        redeem.click()
        time.sleep(5)
    else:
        print("Couldn't find the 2nd New York Times link.")

finally:
    driver.quit()
