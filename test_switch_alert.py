# test_switch_alert.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import os
import datetime

# --- CHEMIN VERS CHROMEDRIVER ---
chrome_driver_path = r"C:\Users\espace info\OneDrive - ESPRIT\Bureau\SwitchToAlertTest\chromedriver.exe"
service = Service(chrome_driver_path)

# --- INITIALISATION DU NAVIGATEUR ---
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# --- URL DU SITE ---
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

# --- DOSSIER POUR LES CAPTURES D'ÉCRAN ---
screenshots_dir = os.path.join(os.getcwd(), "screenshots")
os.makedirs(screenshots_dir, exist_ok=True)

# --- FICHIER DE LOG ---
log_file = os.path.join(os.getcwd(), "test_log.txt")

def log_result(message):
    """Écrire les résultats dans le fichier log (UTF-8)"""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def save_screenshot(name):
    """Enregistrer capture d'écran avec timestamp pour éviter l'écrasement"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(filepath)
    return filepath

# --- 1. Test de l'alerte simple ---
try:
    input_field = driver.find_element(By.ID, "name")
    input_field.send_keys("Hanine")

    alert_button = driver.find_element(By.ID, "alertbtn")
    alert_button.click()

    # Attendre l'apparition de l'alerte
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Message de l'alerte simple :", alert_text)

    # Assertion stricte
    expected_text = "Hello Hanine, share this practice page and share your knowledge"
    assert expected_text == alert_text, f"Message incorrect : attendu '{expected_text}', obtenu '{alert_text}'"
    
    alert.accept()
    print("✅ Message correct")
    log_result(f"Alerte simple : {alert_text} -> ✅ OK")

except (NoAlertPresentException, TimeoutException, AssertionError) as e:
    print(f"❌ Test alerte simple échoué : {e}")
    screenshot_path = save_screenshot("failed_alert")
    print(f"📸 Capture d'écran enregistrée : {screenshot_path}")
    log_result(f"Alerte simple échouée : {e} -> 📸 {screenshot_path}")

# --- 2. Test de l'alerte de confirmation ---
try:
    confirm_button = driver.find_element(By.ID, "confirmbtn")
    confirm_button.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    confirm_alert = driver.switch_to.alert
    confirm_text = confirm_alert.text
    print("Message de l'alerte de confirmation :", confirm_text)

    expected_confirm_text = "Hello , Are you sure you want to confirm?"
    assert expected_confirm_text == confirm_text, f"Confirmation incorrecte : attendu '{expected_confirm_text}', obtenu '{confirm_text}'"

    # OK
    confirm_alert.accept()
    print("✅ Confirmation acceptée")
    log_result(f"Alerte confirmation OK : {confirm_text} -> ✅ OK")

    # Cancel
    confirm_button.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    confirm_alert = driver.switch_to.alert
    confirm_alert.dismiss()
    print("✅ Confirmation annulée")
    log_result(f"Alerte confirmation Cancel : {confirm_text} -> ✅ Cancel")

except (NoAlertPresentException, TimeoutException, AssertionError) as e:
    print(f"❌ Test alerte de confirmation échoué : {e}")
    screenshot_path = save_screenshot("failed_confirm")
    print(f"📸 Capture d'écran enregistrée : {screenshot_path}")
    log_result(f"Alerte confirmation échouée : {e} -> 📸 {screenshot_path}")

# --- 3. Capture d'écran finale ---
final_screenshot = os.path.join(screenshots_dir, "result_screenshot.png")
driver.save_screenshot(final_screenshot)
print("📸 Capture finale enregistrée :", final_screenshot)

# --- 4. Fermeture du navigateur ---
driver.quit()
