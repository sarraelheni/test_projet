from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer le driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

print("----- TC-2 : Bouton Practice -----")

# Localiser le bouton Practice
practice_button = driver.find_element(By.ID, "openwindow")

# Au lieu de réellement ouvrir une nouvelle fenêtre, on simule un bug
driver.execute_script('alert("Le bouton Practice ne fonctionne pas !");')
alert = driver.switch_to.alert
print("Alerte affichée :", alert.text)

# Laisser l'alerte visible pendant 5 secondes
time.sleep(5)
alert.accept()
print("Alerte fermée")

time.sleep(2)
driver.quit()