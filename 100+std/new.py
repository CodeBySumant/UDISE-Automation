from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
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
input_element.send_keys("xde75RN#")

time.sleep(10)

login_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, "submit-btn"))
)
login_button.click()

time.sleep(25)

# Initialize a counter and a flag to control the loop
# Setup WebDriver (as you have already done)
# [...]

row_count = 0
restart_loop = True

while restart_loop:
    restart_loop = False  # Reset the flag at the start of each iteration

    try:
        # Re-find all rows dynamically in case of page change
        rows = driver.find_elements(By.XPATH, "//tbody/tr")
        
        for row in rows:
            try:
                # Progression Status
                Select(row.find_element(By.XPATH, ".//td[2]/ul/li[1]/select")).select_by_index(1)

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
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[6]/button[3]"))).click()
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[6]/button[1]"))).click()
                time.sleep(1)

                # Increment the row counter
                row_count += 1

                # Pause for 10 seconds after every 100 rows
                if row_count > 0 and row_count % 100 == 0:
                    print(f"Processed {row_count} rows. Pausing for 10 seconds...")
                    time.sleep(10)

                    # Scroll to the top of the page
                    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
                    time.sleep(1)

                    # Find and click the "Next Page" button
                    try:
                        next_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-admin-dashboard/div[2]/div[2]/main/div/div/div/app-promotion/div[3]/div/table/tbody/tr[1]/following::button[2]"))
                        )
                        next_button.click()

                        # Wait for the next page to load
                        time.sleep(5)

                        # Recollect rows from the next page
                        rows = driver.find_elements(By.XPATH, "//tbody/tr")

                    except NoSuchElementException:
                        print("No more pages. Script completed.")
                        restart_loop = False
                        break

                    time.sleep(1)

            except (ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException) as e:
                print(f"Error processing row {row_count}: {e}")
                restart_loop = True  # Set flag to restart loop in case of error
                break  # Exit the for loop to re-find elements

    except Exception as e:
        print(f"Error: {e}")
        break  # Exit the while loop if a major error occurs

print("Script completed.")
