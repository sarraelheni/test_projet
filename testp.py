from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(URL)

time.sleep(2)

try:
    # Descendre jusqu'en bas
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Trouver le lien YouTube
    link = driver.find_element(By.LINK_TEXT, "Youtube")

    # Compter onglets avant clic
    before_tabs = len(driver.window_handles)

    # Cliquer
    ActionChains(driver).move_to_element(link).click().perform()
    time.sleep(3)

    # Compter onglets après clic
    after_tabs = len(driver.window_handles)

    if after_tabs == before_tabs:
        # Alerte console
        print("ALERTE : Le lien YouTube ne fonctionne pas. Aucun nouvel onglet n'a été ouvert.")

        # Alerte visuelle pour toi (popup JavaScript)
        driver.execute_script("alert('Le lien YouTube ne fonctionne pas. Aucun nouvel onglet ne s\\'est ouvert.');")
        time.sleep(4)

    else:
        print("Le lien YouTube fonctionne : un nouvel onglet a été ouvert.")

except Exception as e:
    print("Erreur lors du test.")
    print("Détails :", e)

finally:
    time.sleep(3)
    driver.quit()
