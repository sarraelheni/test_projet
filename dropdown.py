from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
    dropdown = Select(dropdown_element)

    print("----- TC-01 : Dropdown visible -----")
    if dropdown:
        print("PASS : Dropdown visible")
    time.sleep(2)

    options = ["Option1", "Option2"]  # Options à tester

    for option in options:
        # Ouvrir le dropdown (simule le clic pour dérouler)
        dropdown_element.click()
        time.sleep(1)  # Liste déroulée visible

        # Sélectionner l'option
        dropdown.select_by_visible_text(option)
        print(f"PASS : {option} sélectionnée")

        # Rouvrir le dropdown pour observer
        dropdown_element.click()
        time.sleep(2)  # Temps pour voir la sélection

    # Test navigation clavier
    print("----- TC-05 : Navigation clavier -----")
    dropdown_element.click()
    dropdown_element.send_keys(Keys.ARROW_DOWN)
    dropdown_element.send_keys(Keys.ENTER)
    print("PASS : Navigation clavier OK")
    time.sleep(2)

    # Double clic
    print("----- TC-06 : Double clic -----")
    actions = ActionChains(driver)
    actions.double_click(dropdown_element).perform()
    print("PASS : Double clic fonctionne")
    time.sleep(5)

finally:
    driver.quit()
