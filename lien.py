# -------------------------------------------------
# SCRIPT SELENIUM PYTHON POUR TESTER LE LIEN "Medianh Consulting" AVEC SCROLL
# -------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)

   
    medianh_link = driver.find_element(By.LINK_TEXT, "Medianh Consulting")

    
    actions = ActionChains(driver)
    actions.move_to_element(medianh_link).perform()
    print("Scroll effectué jusqu'au lien.")

   
    link_url = medianh_link.get_attribute("href")
    print(f"URL du lien : {link_url}")

    
    try:
        response = requests.head(link_url, timeout=5)
        if response.status_code == 200:
            print("Le lien est valide (200 OK)")
        elif response.status_code == 404:
            print("Le lien est cassé (404 Not Found)")
        else:
            print(f"Le lien renvoie le statut : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")

  
    medianh_link.click()
    time.sleep(5) 
    if "Page Not Found" in driver.page_source or "404" in driver.page_source:
        print("Le clic sur le lien mène vers une page 404 (lien cassé)")
    else:
        print("Le lien fonctionne correctement après clic")

finally:
   
    driver.quit()
