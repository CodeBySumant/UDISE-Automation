from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Setup WebDriver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://sdms.udiseplus.gov.in/p0/v1/login")
driver.maximize_window()

# Login
input_element = driver.find_element(By.CLASS_NAME, "form-control")
input_element.send_keys("10140601611")

input_element = driver.find_element(By.ID, "password-field")
input_element.send_keys("VG65qrq#")

time.sleep(10)

login_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "submit-btn"))
)
login_button.click()

time.sleep(25)

# Find all rows in the table dynamically
rows = driver.find_elements(By.XPATH, "//tbody/tr")

time.sleep(2)

# Total number of rows
total_rows = len(rows)

# Process each row with a 10-second pause before processing every 100 rows
for i in range(total_rows):
    # Pause for 10 seconds before processing the next 100 rows
    if i > 0 and i % 100 == 0:
        print(f"Processed {i} rows. Pausing for 10 seconds...")
        time.sleep(10)

    row = rows[i]

    # Progression Status
    Select(row.find_element(By.XPATH, ".//td[2]/ul/li[1]/select")).select_by_index(1)
    time.sleep(1)

    # Generate a random number between 70 and 90 for Marks in %
    random_number = random.randint(70, 90)
    input_field = row.find_element(By.XPATH, ".//td[2]/ul/li[2]/input")
    input_field.clear()
    input_field.send_keys(str(random_number))

    # Generate a random number between 200 and 230 for No. of Days School attended
    random_number = random.randint(200, 230)
    input_field = row.find_element(By.XPATH, ".//td[2]/ul/li[3]/input")
    input_field.clear()
    input_field.send_keys(str(random_number))

    # Schooling Status
    Select(row.find_element(By.XPATH, ".//td[2]/ul/li[4]/select")).select_by_index(1)

    # Click Update
    row.find_element(By.XPATH, ".//td[6]/button[1]").click()
    time.sleep(2)

    # Click on confirm
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[6]/button[3]").click()
    time.sleep(2)

    # Click on confirm
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[6]/button[1]").click()
    time.sleep(2)

print("All rows processed.")
