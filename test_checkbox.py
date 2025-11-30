from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://rahulshettyacademy.com/AutomationPractice/"


def tester_checkbox(driver, checkbox_id: str) -> None:
    """
    Teste une checkbox en la cochant puis en la décochant
    et en vérifiant son état à chaque étape.
    Lève une Exception en cas d'anomalie.
    """
    element = driver.find_element(By.ID, checkbox_id)

    # 1) Clic pour cocher
    element.click()
    time.sleep(0.5)  # petite pause pour la mise à jour de l'UI

    if not element.is_selected():
        message = f"[ERREUR] Après clic, la checkbox {checkbox_id} n'est pas cochée."
        print(message)
        driver.execute_script(f"alert('{message}');")
        time.sleep(3)
        raise Exception(message)

    # 2) Clic pour décocher
    element.click()
    time.sleep(0.5)

    if element.is_selected():
        message = f"[ERREUR] Après second clic, la checkbox {checkbox_id} est encore cochée."
        print(message)
        driver.execute_script(f"alert('{message}');")
        time.sleep(3)
        raise Exception(message)

    print(f"[OK] Checkbox {checkbox_id} : comportement coche/décoche correct.")


def tester_toutes_les_checkboxes(driver) -> None:
    """
    Enchaîne les tests sur les trois checkboxes principales,
    puis vérifie la sélection simultanée des trois.
    """
    checkbox_ids = ["checkBoxOption1", "checkBoxOption2", "checkBoxOption3"]

    print("=== Étape 1 : Test individuel coche/décoche ===")
    for cid in checkbox_ids:
        tester_checkbox(driver, cid)

    print("\n=== Étape 2 : Test de la sélection simultanée des trois checkboxes ===")
    # Cocher toutes les cases
    for cid in checkbox_ids:
        element = driver.find_element(By.ID, cid)
        if not element.is_selected():
            element.click()
            time.sleep(0.3)

    # Vérifier que toutes sont cochées
    toutes_cochees = True
    for cid in checkbox_ids:
        element = driver.find_element(By.ID, cid)
        if not element.is_selected():
            toutes_cochees = False
            print(f"[ERREUR] La checkbox {cid} devrait être cochée dans le scénario 'toutes cochées'.")

    if not toutes_cochees:
        message = "[ERREUR] Une ou plusieurs checkboxes ne sont pas cochées alors qu'elles devraient l'être."
        driver.execute_script(f"alert('{message}');")
        time.sleep(3)
        raise Exception(message)

    print("[OK] Les trois checkboxes peuvent être cochées simultanément.")


def main():
    # Initialisation du driver Chrome via WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(URL)

    # Attente explicite que la section checkbox soit présente
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "checkBoxOption1")))
    time.sleep(1)

    try:
        print("========== DÉBUT DU TEST AUTOMATISÉ : CHECKBOXES ==========")
        tester_toutes_les_checkboxes(driver)
        print("\n[RÉSUMÉ] Toutes les vérifications sur les checkboxes sont PASS.")
    except Exception as e:
        print("\n[RÉSUMÉ] Une anomalie a été détectée pendant le test automatique des checkboxes.")
        print("Détail de l'erreur :", e)
    finally:
        time.sleep(3)
        driver.quit()
        print("Navigateur fermé. Fin du test.")


if __name__ == "__main__":
    main()
