from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://sdms.udiseplus.gov.in/p0/v1/login")
driver.maximize_window()

# Login
input_element = driver.find_element(By.CLASS_NAME, "form-control")
input_element.send_keys("10140806703")

input_element = driver.find_element(By.ID, "password-field")
input_element.send_keys("#sfkIG35")

time.sleep(10)  # Let the page load

# Click login button
login_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, "submit-btn"))
)
login_button.click()

time.sleep(25)  # Wait for dashboard to load

while True:
    time.sleep(2)

    # ✅ Click the "Correction" button
    try:
        correction_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Correction")]'))
        )
        correction_button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", correction_button)

    time.sleep(1)

    # ✅ Select from first dropdown
    try:
        dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-select"))
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//select[@class="form-select"]//option[@value="5"]'))
        )

        select = Select(dropdown)
        select.select_by_value("5")
    except NoSuchElementException:
        print("Dropdown option '5' not found!")

    time.sleep(1)

    # ✅ Select from second dropdown
    try:
        next_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-select-sm"))
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//select[@class="form-select-sm"]//option[@value="2"]'))
        )

        select_next = Select(next_dropdown)
        select_next.select_by_value("2")
    except NoSuchElementException:
        print("Dropdown option '2' not found!")

    time.sleep(1)

    # ✅ Click the "Update" button
    try:
        update_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Update")]'))
        )
        update_button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", update_button)

    time.sleep(1)

    # ✅ Click the "Confirm" button
    try:
        confirm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "swal2-cancel"))
        )
        confirm_button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", confirm_button)

    time.sleep(1)

    # ✅ Click the "Okay" button
    try:
        okay_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm"))
        )
        okay_button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", okay_button)

    time.sleep(3)
