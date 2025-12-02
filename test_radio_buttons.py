from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer le driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    print("----- TC-01 : Test complet des boutons radio -----")

    # Localiser tous les boutons radio
    radio_buttons = driver.find_elements(By.NAME, "radioButton")
    total = len(radio_buttons)
    print(f"Nombre total de boutons radio trouvés : {total}")

    for i, radio in enumerate(radio_buttons, start=1):
        print(f"\n--- Test du bouton radio {i} ---")

        # Vérifier la visibilité
        if radio.is_displayed():
            print("PASS : Bouton visible")
        else:
            print("FAIL : Bouton non visible")

        # Sélectionner le bouton
        radio.click()
        print("Action : Bouton cliqué")

        # Vérifier la sélection
        if radio.is_selected():
            print("PASS : Bouton sélectionné correctement")
        else:
            print("FAIL : Sélection échouée")

        # Petite pause pour observer l'action
        time.sleep(3)

    print("\nTous les boutons radio ont été testés.")

    time.sleep(5)

finally:
    driver.quit()
