from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

CLASS1_HEIGHT_UPPER = 145
CLASS1_HEIGHT_LOWER = 150
CLASS1_WEIGHT_UPPER = 45       
CLASS1_WEIGHT_LOWER = 50

def generate_random_integer(start, end):
    return str(random.randint(start, end))

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://sdms.udiseplus.gov.in/p0/v1/login?state-id=110")
driver.maximize_window()

input_element = driver.find_element(By.CLASS_NAME, "form-control")
input_element.send_keys("BR71392670")

input_element = driver.find_element(By.ID, "password-field")
input_element.send_keys("ODdgp53#")

time.sleep(10)

login_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "submit-btn"))
)
login_button.click()

time.sleep(25)

while True:
    time.sleep(2)

    # blood group 
    blood_group_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@formcontrolname="bloodGroup"]'))
    )
    blood_group_select = Select(blood_group_dropdown)
    blood_group_select.select_by_value("9")

    # Click on update button
    update_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space(span/text())='Save']"))
    )
    update_button.click()

    time.sleep(1)
    # Wait for the close button to be present in the DOM
    wait = WebDriverWait(driver, 20)  # Adjust the timeout as needed
    close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline")))

    # Click the close button
    close_button.click()

    next_button_xpath = '//button[@type="button" and @matsteppernext]'
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, next_button_xpath))
    )
    next_button.click()

    time.sleep(2)

    # date select
    date_input_xpath = '//input[@formcontrolname="admnStartDate"]'
    date_input_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, date_input_xpath))
    )
    driver.execute_script("arguments[0].click();", date_input_element)
    date_input_element.send_keys("04/04/2023", Keys.ENTER)

    # Locate the <select> element
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname='languageGroup']"))
    )

    # Create a Select object
    dropdown = Select(select_element)

    # Select by value
    dropdown.select_by_value("1002")

    dynamic_xpath_value_2 = "//select[@formcontrolname='academicStream']/option[@value='2']"

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "swal2-cancel"))
    )
    button.click()
    time.sleep(2)

    radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="centralScholarship"]'))
    )
    radio_button.click()

    second_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="stateScholarship"]'))
    )
    second_radio_button.click()

    third_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="otherScholarship"]'))
    )
    third_radio_button.click()

    forth_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="screenedForSld"]'))
    )
    forth_radio_button.click()

    fifth_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="autismSpectrumDisorder"]'))
    )
    fifth_radio_button.click()

    sixth_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="attentionDeficitHyperactiveDisorder"]'))
    )
    sixth_radio_button.click()

    seventh_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @name="extracurricularActivity" and @formcontrolname="isEcActivity"]'))
    )
    seventh_radio_button.click()

    eigth_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @formcontrolname="giftedYN"]'))
    )
    eigth_radio_button.click()

    nnieth_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @name="NCC" and @formcontrolname="nccNssYn"]'))
    )
    nnieth_radio_button.click()

    tenth_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="radio" and @value="2" and @name="DGC" and @formcontrolname="digitalCapableYn"]'))
    )
    tenth_radio_button.click()

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @formcontrolname="heightInCm"]'))
    )
    input_field.clear()
    input_field.send_keys(generate_random_integer(CLASS1_HEIGHT_UPPER, CLASS1_HEIGHT_LOWER))

    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @formcontrolname="weightInKg"]'))
    )
    input_element.clear()
    input_element.send_keys(generate_random_integer(CLASS1_WEIGHT_UPPER, CLASS1_WEIGHT_LOWER), Keys.ENTER)
    time.sleep(2)

    fss_button_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and @class="swal2-cancel swal2-styled swal2-default-outline"]'))
    )
    fss_button_element.click()

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    complete_data_button_xpath = '//button[contains(@class, "btnsave") and contains(@class, "float-end")]'
    complete_data_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, complete_data_button_xpath))
    )
    driver.execute_script("arguments[0].click();", complete_data_button)

    ffinal_button_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and contains(@class, "swal2-cancel")]'))
    )
    ffinal_button_element.click()

    nnex_button_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="button" and contains(@class, "swal2-cancel") and contains(text(), "Next Student")]'))
    )
    nnex_button_element.click()
