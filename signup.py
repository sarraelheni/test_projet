from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer le driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    print("----- TC-07 : Simuler alerte SignUp ne marche pas -----")

    # Exécuter du JavaScript pour créer une alerte personnalisée
    driver.execute_script('alert("Le bouton SignUp ne fonctionne pas !");')

    # Passer sur l'alerte
    alert = driver.switch_to.alert
    print("Texte de l'alerte :", alert.text)

    # Maintenir l'alerte visible 5 secondes
    time.sleep(5)

    # Accepter l'alerte
    alert.accept()
    print("Alerte acceptée")

finally:
    driver.quit()
