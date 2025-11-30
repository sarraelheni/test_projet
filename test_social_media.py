from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://rahulshettyacademy.com/AutomationPractice/"
SOCIAL_LABELS = ["Facebook", "Twitter", "Google+", "Youtube"]


def trouver_element_par_texte(driver, texte: str):
    """
    Tente de trouver un élément dont le texte visible correspond au libellé.
    Utilise un XPath générique, qui peut cibler un <li>, <span>, <a>, etc.
    """
    xpath = f"//*[normalize-space()='{texte}']"
    try:
        return driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None


def tester_reseau(driver, label: str) -> bool:
    """
    Teste un élément Social Media :
    - vérifie sa présence dans la page,
    - vérifie s'il s'agit d'une balise <a> cliquable,
    - si c'est un lien, teste l'ouverture d'un nouvel onglet.
    Retourne True si le comportement est conforme, False sinon.
    """
    print(f"\n=== Test du réseau : {label} ===")

    element = trouver_element_par_texte(driver, label)
    if element is None:
        print(f"[ERREUR] Aucun élément portant le texte '{label}' n'a été trouvé.")
        return False

    tag = element.tag_name.lower()
    print(f"Balise HTML pour '{label}' détectée : <{tag}>")

    # Si ce n'est pas un lien <a>, c'est une anomalie (texte statique)
    if tag != "a":
        print(f"[ANOMALIE] '{label}' est affiché comme du texte (<{tag}>) et non comme un lien <a> cliquable.")
        return False

    href = element.get_attribute("href")
    print(f"URL de destination pour '{label}' : {href}")

    if not href:
        print(f"[ANOMALIE] Le lien <a> pour '{label}' ne possède pas d'attribut href valide.")
        return False

    before_tabs = len(driver.window_handles)

    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    time.sleep(3)
    after_tabs = len(driver.window_handles)

    if after_tabs <= before_tabs:
        print(f"[ANOMALIE] Après clic sur '{label}', aucun nouvel onglet n'a été ouvert.")
        return False

    print(f"[OK] Le lien '{label}' a ouvert un nouvel onglet comme attendu.")
    return True


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(URL)

    wait = WebDriverWait(driver, 10)
    # Attendre qu'un élément du bas de page soit présent
    wait.until(EC.presence_of_element_located((By.ID, "mousehover")))

    # Scroller tout en bas pour rendre la section Social Media visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    print("========== DÉBUT DU TEST AUTOMATISÉ : SOCIAL MEDIA ==========")

    nb_tests = 0
    nb_pass = 0

    try:
        for label in SOCIAL_LABELS:
            nb_tests += 1
            ok = tester_reseau(driver, label)
            if ok:
                nb_pass += 1

        print("\n========== RÉSUMÉ DU TEST SOCIAL MEDIA ==========")
        print(f"Nombre total de réseaux testés : {nb_tests}")
        print(f"Nombre de réseaux conformes    : {nb_pass}")
        print(f"Nombre de réseaux en anomalie  : {nb_tests - nb_pass}")

        if nb_pass == nb_tests:
            print("[RÉSUMÉ] Tous les liens Social Media fonctionnent correctement.")
        else:
            print("[RÉSUMÉ] Des anomalies ont été détectées sur la section Social Media.")
            driver.execute_script(
                "alert('Des anomalies ont été détectées sur les liens Social Media (Facebook / Twitter / Google+ / Youtube).');"
            )
            time.sleep(4)

    except Exception as e:
        print("[ERREUR GÉNÉRALE] Une exception est survenue pendant le test Social Media.")
        print("Détails :", e)

    finally:
        time.sleep(3)
        driver.quit()
        print("Navigateur fermé. Fin du test Social Media.")


if __name__ == "__main__":
    main()
