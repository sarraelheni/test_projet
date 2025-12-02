from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)

   
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    
    broken_link = driver.find_element(By.LINK_TEXT, "Broken Link")


    link_url = broken_link.get_attribute("href")
    print(f"URL du lien : {link_url}")

    
    response = requests.head(link_url)
    if response.status_code == 200:
        print("Le lien est valide (200 OK)")
    elif response.status_code == 404:
        print("Le lien est cassé (404 Not Found)")
    else:
        print(f"Le lien renvoie le statut : {response.status_code}")

    
    broken_link.click()
    time.sleep(3)  
    if "Page Not Found" in driver.page_source:
        print("Le clic sur le lien mène vers une page 404")
    else:
        print("Le lien fonctionne correctement après clic")

finally:
    driver.quit()
