"""
Test automatisé : Switch Window Example
Site : https://rahulshettyacademy.com/AutomationPractice/
Auteur : Bouchoucha Yomna
Date : 2025
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_switch_window():
    """
    Test automatisé pour la fonctionnalité Switch Window
    Vérifie l'ouverture, la navigation et la fermeture de nouvelles fenêtres
    """
    print("="*60)
    print("DEBUT DU TEST : Switch Window Example")
    print("="*60)
    
    # Configuration du driver Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Etape 1 : Accès à la page de test
        print("\n[ETAPE 1] Navigation vers la page de test...")
        url = "https://rahulshettyacademy.com/AutomationPractice/"
        driver.get(url)
        print(f"✓ URL chargée : {driver.current_url}")
        time.sleep(2)
        
        # Etape 2 : Vérification du nombre initial de fenêtres
        print("\n[ETAPE 2] Vérification des fenêtres initiales...")
        initial_handles = driver.window_handles
        print(f"Nombre de fenêtres initial : {len(initial_handles)}")
        assert len(initial_handles) == 1, "Erreur : Plus d'une fenêtre au début"
        print("✓ Test réussi : Une seule fenêtre initialement")
        
        # Etape 3 : Clic sur le bouton "Open Window"
        print("\n[ETAPE 3] Clic sur le bouton 'Open Window'...")
        open_window_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "openwindow"))
        )
        open_window_btn.click()
        print("✓ Bouton cliqué avec succès")
        time.sleep(3)
        
        # Etape 4 : Vérification du nombre de fenêtres après ouverture
        print("\n[ETAPE 4] Vérification de l'ouverture de la nouvelle fenêtre...")
        all_handles = driver.window_handles
        print(f"Nombre de fenêtres après ouverture : {len(all_handles)}")
        assert len(all_handles) == 2, "Erreur : La nouvelle fenêtre ne s'est pas ouverte"
        print("✓ Test réussi : Nouvelle fenêtre ouverte")
        
        # Etape 5 : Switch vers la nouvelle fenêtre
        print("\n[ETAPE 5] Basculement vers la nouvelle fenêtre...")
        new_window = [handle for handle in all_handles if handle != initial_handles[0]][0]
        driver.switch_to.window(new_window)
        print(f"✓ Fenêtre active : {driver.current_window_handle}")
        time.sleep(2)
        
        # Etape 6 : Vérification du titre de la nouvelle fenêtre
        print("\n[ETAPE 6] Vérification du titre de la nouvelle fenêtre...")
        new_window_title = driver.title
        print(f"Titre : {new_window_title}")
        assert "QAClick" in new_window_title, "Erreur : Titre incorrect"
        print("✓ Test réussi : Titre correct")
        
        # Etape 7 : Vérification de l'URL de la nouvelle fenêtre
        print("\n[ETAPE 7] Vérification de l'URL de la nouvelle fenêtre...")
        new_window_url = driver.current_url
        print(f"URL : {new_window_url}")
        assert "qaclickacademy" in new_window_url.lower(), "Erreur : URL incorrecte"
        print("✓ Test réussi : URL correcte")
        
        # Etape 8 : Retour à la fenêtre principale
        print("\n[ETAPE 8] Retour à la fenêtre principale...")
        driver.switch_to.window(initial_handles[0])
        time.sleep(2)
        
        # Etape 9 : Vérification du retour
        print("\n[ETAPE 9] Vérification du retour...")
        main_url = driver.current_url
        assert "AutomationPractice" in main_url, "Erreur : Pas revenu à la fenêtre principale"
        print("✓ Test réussi : Retour réussi")
        
        # Etape 10 : Fermeture de la nouvelle fenêtre
        print("\n[ETAPE 10] Fermeture de la nouvelle fenêtre...")
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(initial_handles[0])
        time.sleep(1)
        
        # Etape 11 : Vérification finale
        print("\n[ETAPE 11] Vérification finale...")
        final_handles = driver.window_handles
        print(f"Nombre de fenêtres final : {len(final_handles)}")
        assert len(final_handles) == 1, "Erreur : La fenêtre n'a pas été fermée"
        print("✓ Test réussi : Fenêtre fermée correctement")
        
        print("\n" + "="*60)
        print("✓✓✓ RESULTAT : TOUS LES TESTS ONT REUSSI ✓✓✓")
        print("="*60)
        
    except AssertionError as ae:
        print(f"\n❌ ECHEC DU TEST : {str(ae)}")
        screenshot_name = f"error_switch_window_{int(time.time())}.png"
        driver.save_screenshot(screenshot_name)
        print(f"📸 Capture d'écran sauvegardée : {screenshot_name}")
        
    except Exception as e:
        print(f"\n❌ ERREUR INATTENDUE : {str(e)}")
        screenshot_name = f"error_switch_window_{int(time.time())}.png"
        driver.save_screenshot(screenshot_name)
        print(f"📸 Capture d'écran sauvegardée : {screenshot_name}")
        
    finally:
        print("\n[FERMETURE] Fermeture du navigateur...")
        time.sleep(2)
        driver.quit()
        print("✓ Navigateur fermé avec succès\n")

if __name__ == "__main__":
    test_switch_window()

"""
Test automatisé : Switch Tab Example
Site : https://rahulshettyacademy.com/AutomationPractice/
Auteur : Bouchoucha Yomna
Date : 2025
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_switch_tab():
    """
    Test automatisé pour la fonctionnalité Switch Tab
    Vérifie l'ouverture, la navigation et la fermeture de nouveaux onglets
    """
    print("="*60)
    print("DEBUT DU TEST : Switch Tab Example")
    print("="*60)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Etape 1 : Navigation vers la page
        print("\n[ETAPE 1] Navigation vers la page de test...")
        url = "https://rahulshettyacademy.com/AutomationPractice/"
        driver.get(url)
        print(f"✓ URL chargée : {driver.current_url}")
        time.sleep(2)
        
        # Etape 2 : Vérification des onglets initiaux
        print("\n[ETAPE 2] Vérification des onglets initiaux...")
        initial_tabs = driver.window_handles
        print(f"Nombre d'onglets initial : {len(initial_tabs)}")
        assert len(initial_tabs) == 1, "Erreur : Plus d'un onglet au début"
        print("✓ Test réussi : Un seul onglet initialement")
        
        # Etape 3 : Localisation et clic sur "Open Tab"
        print("\n[ETAPE 3] Clic sur le lien 'Open Tab'...")
        open_tab_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "opentab"))
        )
        open_tab_link.click()
        print("✓ Lien cliqué avec succès")
        time.sleep(3)
        
        # Etape 4 : Vérification de l'ouverture du nouvel onglet
        print("\n[ETAPE 4] Vérification de l'ouverture du nouvel onglet...")
        all_tabs = driver.window_handles
        print(f"Nombre d'onglets après ouverture : {len(all_tabs)}")
        assert len(all_tabs) == 2, "Erreur : Le nouvel onglet ne s'est pas ouvert"
        print("✓ Test réussi : Nouvel onglet ouvert")
        
        # Etape 5 : Switch vers le nouvel onglet
        print("\n[ETAPE 5] Basculement vers le nouvel onglet...")
        new_tab = [tab for tab in all_tabs if tab != initial_tabs[0]][0]
        driver.switch_to.window(new_tab)
        print(f"✓ Onglet actif : {driver.current_window_handle}")
        time.sleep(3)
        
        # Etape 6 : Vérification de l'URL du nouvel onglet
        print("\n[ETAPE 6] Vérification de l'URL du nouvel onglet...")
        new_tab_url = driver.current_url
        print(f"URL : {new_tab_url}")
        assert "qaclickacademy" in new_tab_url.lower(), "Erreur : URL incorrecte"
        print("✓ Test réussi : URL correcte")
        
        # Etape 7 : Vérification du titre du nouvel onglet
        print("\n[ETAPE 7] Vérification du titre du nouvel onglet...")
        new_tab_title = driver.title
        print(f"Titre : {new_tab_title}")
        assert len(new_tab_title) > 0, "Erreur : Titre vide"
        print("✓ Test réussi : Titre présent")
        
        # Etape 8 : Retour à l'onglet principal
        print("\n[ETAPE 8] Retour à l'onglet principal...")
        driver.switch_to.window(initial_tabs[0])
        time.sleep(2)
        
        # Etape 9 : Vérification du retour
        print("\n[ETAPE 9] Vérification du retour...")
        main_tab_url = driver.current_url
        assert "AutomationPractice" in main_tab_url, "Erreur : Pas revenu à l'onglet principal"
        print("✓ Test réussi : Retour réussi")
        
        # Etape 10 : Vérification du contenu de l'onglet principal
        print("\n[ETAPE 10] Vérification du contenu...")
        try:
            open_tab_link_check = driver.find_element(By.ID, "opentab")
            print("✓ Test réussi : Contenu intact")
        except:
            raise AssertionError("Erreur : Element 'opentab' non trouvé")
        
        # Etape 11 : Fermeture du nouvel onglet
        print("\n[ETAPE 11] Fermeture du nouvel onglet...")
        driver.switch_to.window(new_tab)
        driver.close()
        driver.switch_to.window(initial_tabs[0])
        time.sleep(1)
        
        # Etape 12 : Vérification finale
        print("\n[ETAPE 12] Vérification finale...")
        final_tabs = driver.window_handles
        print(f"Nombre d'onglets final : {len(final_tabs)}")
        assert len(final_tabs) == 1, "Erreur : L'onglet n'a pas été fermé"
        print("✓ Test réussi : Onglet fermé correctement")
        
        print("\n" + "="*60)
        print("✓✓✓ RESULTAT : TOUS LES TESTS ONT REUSSI ✓✓✓")
        print("="*60)
        
    except AssertionError as ae:
        print(f"\n❌ ECHEC DU TEST : {str(ae)}")
        screenshot_name = f"error_switch_tab_{int(time.time())}.png"
        driver.save_screenshot(screenshot_name)
        print(f"📸 Capture d'écran sauvegardée : {screenshot_name}")
        
    except Exception as e:
        print(f"\n❌ ERREUR INATTENDUE : {str(e)}")
        screenshot_name = f"error_switch_tab_{int(time.time())}.png"
        driver.save_screenshot(screenshot_name)
        print(f"📸 Capture d'écran sauvegardée : {screenshot_name}")
    finally:
        driver.quit()
"""
Test automatise : Element Displayed Example (Hide/Show)
Site : https://rahulshettyacademy.com/AutomationPractice/
Auteur : Bouchoucha Yomna
Date : 2025

VALIDATION DU BUG BUG-HS-001 : Comportement toggle au lieu de hide/show
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestHideShow:
    """Classe de test pour Hide/Show Element"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "https://rahulshettyacademy.com/AutomationPractice/"
        self.wait = WebDriverWait(self.driver, 10)
        
        self.tests_passed = 0
        self.tests_failed = 0
        self.bugs_found = []
        
    def setup(self):
        """Configuration initiale"""
        print("="*70)
        print("DEBUT DU TEST : Element Displayed Example (Hide/Show)")
        print("="*70)
        print(f"\n[SETUP] Navigation vers : {self.url}")
        self.driver.get(self.url)
        time.sleep(2)
        print(f"✓ Page chargée : {self.driver.title}")
        
    def take_screenshot(self, name):
        """Capture d'écran en cas d'erreur"""
        filename = f"{name}.png"
        self.driver.save_screenshot(filename)
        print(f"[+] Screenshot enregistré : {filename}")

    # -------------------------------------------------------
    # TEST 1 : Vérifier que l'élément est visible au départ
    # -------------------------------------------------------
    def test_01_initial_state_visible(self):
        print("\n" + "="*70)
        print("TEST 1 : Verification de l'état initial")
        print("="*70)
        
        try:
            element = self.wait.until(
                EC.presence_of_element_located((By.ID, "displayed-text"))
            )
            is_visible = element.is_displayed()
            print(f"État initial : {'Visible' if is_visible else 'Caché'}")
            
            assert is_visible == True, "❌ ECHEC : L'élément devrait être visible initialement"
            print("✓ (TC-AUTO-HS-01 PASS)")
            self.tests_passed += 1
            return True
            
        except Exception as e:
            print(f"\n❌ TEST 1 ECHOUE : {str(e)}")
            self.take_screenshot("test01_failed")
            self.tests_failed += 1
            return False

    # -------------------------------------------------------
    # TEST 2 : Cacher l'élément
    # -------------------------------------------------------
    def test_02_hide_element(self):
        print("\n" + "="*70)
        print("TEST 2 : Cacher l'élément (Hide)")
        print("="*70)
        
        try:
            hide_button = self.driver.find_element(By.ID, "hide-textbox")
            element = self.driver.find_element(By.ID, "displayed-text")

            print("Clic sur Hide…")
            hide_button.click()
            time.sleep(1)

            after_state = element.is_displayed()
            print(f"État après Hide : {'Visible' if after_state else 'Caché'}")

            assert after_state is False, "❌ L'élément devrait être caché"
            print("✓ (TC-AUTO-HS-02 PASS)")
            self.tests_passed += 1
            return True
            
        except Exception as e:
            print(f"\n❌ TEST 2 ECHOUE : {str(e)}")
            self.take_screenshot("test02_failed")
            self.tests_failed += 1
            return False


    # -------------------------------------------------------
    # TEST 3 : Afficher l'élément via Show
    # -------------------------------------------------------
    def test_03_show_element(self):
        print("\n" + "="*70)
        print("TEST 3 : Afficher l'élément (Show)")
        print("="*70)
        
        try:
            hide_button = self.driver.find_element(By.ID, "hide-textbox")
            show_button = self.driver.find_element(By.ID, "show-textbox")
            element = self.driver.find_element(By.ID, "displayed-text")

            # S'assurer qu'il est caché
            if element.is_displayed():
                hide_button.click()
                time.sleep(1)

            print("Clic sur Show…")
            show_button.click()
            time.sleep(1)

            is_visible = element.is_displayed()
            print(f"État après Show : {'Visible' if is_visible else 'Caché'}")

            assert is_visible is True, "❌ L'élément devrait être visible"
            print("✓ (TC-AUTO-HS-03 PASS)")
            self.tests_passed += 1
            return True
        
        except Exception as e:
            print(f"\n❌ TEST 3 ECHOUE : {str(e)}")
            self.take_screenshot("test03_failed")
            self.tests_failed += 1
            return False


    # -------------------------------------------------------
    # TEST 4 : BUG - Hide agit comme un toggle
    # -------------------------------------------------------
    def test_04_hide_toggle_bug(self):
        print("\n" + "="*70)
        print("TEST 4 : Vérification du BUG toggle du bouton Hide")
        print("="*70)

        try:
            hide_button = self.driver.find_element(By.ID, "hide-textbox")
            element = self.driver.find_element(By.ID, "displayed-text")

            print("Clic 1 sur Hide…")
            hide_button.click()
            time.sleep(1)

            print("Clic 2 sur Hide…")
            hide_button.click()
            time.sleep(1)

            # BUG : Hide ré-affiche l'élément !
            if element.is_displayed():
                print("❌ BUG détecté : Hide agit comme un toggle.")
                self.bugs_found.append("BUG-HS-001")
            else:
                print("✓ Comportement normal (pas de toggle)")

            print("✓ (TC-AUTO-HS-04 EXECUTE)")
            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"\n❌ TEST 4 ECHOUE : {str(e)}")
            self.take_screenshot("test04_failed")
            self.tests_failed += 1
            return False


    # -------------------------------------------------------
    # TEST 5 : BUG - Show agit comme un toggle
    # -------------------------------------------------------
    def test_05_show_toggle_bug(self):
        print("\n" + "="*70)
        print("TEST 5 : Vérification du BUG toggle du bouton Show")
        print("="*70)

        try:
            show_button = self.driver.find_element(By.ID, "show-textbox")
            element = self.driver.find_element(By.ID, "displayed-text")

            print("Clic 1 sur Show…")
            show_button.click()
            time.sleep(1)

            print("Clic 2 sur Show…")
            show_button.click()
            time.sleep(1)

            # BUG : Show cache l'élément
            if not element.is_displayed():
                print("❌ BUG détecté : Show agit comme un toggle.")
                self.bugs_found.append("BUG-HS-001")
            else:
                print("✓ Comportement normal (pas de toggle)")

            print("✓ (TC-AUTO-HS-05 EXECUTE)")
            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"\n❌ TEST 5 ECHOUE : {str(e)}")
            self.take_screenshot("test05_failed")
            self.tests_failed += 1
            return False


    # -------------------------------------------------------
    # TEST 6 : Alternances rapides
    # -------------------------------------------------------
    def test_06_fast_switch(self):
        print("\n" + "="*70)
        print("TEST 6 : Alternances rapides Hide/Show")
        print("="*70)

        try:
            hide_button = self.driver.find_element(By.ID, "hide-textbox")
            show_button = self.driver.find_element(By.ID, "show-textbox")
            element = self.driver.find_element(By.ID, "displayed-text")

            print("Alternances rapides (10 itérations)…")
            for _ in range(10):
                hide_button.click()
                show_button.click()
                time.sleep(0.2)

            final_state = element.is_displayed()
            print(f"État final : {'Visible' if final_state else 'Caché'}")

            assert final_state is True, "❌ Problème de stabilité après alternances"
            print("✓ (TC-AUTO-HS-06 PASS)")
            self.tests_passed += 1
            return True

        except Exception as e:
            print(f"\n❌ TEST 6 ECHOUE : {str(e)}")
            self.take_screenshot("test06_failed")
            self.tests_failed += 1
            return False


    # -------------------------------------------------------
    # FIN DU TEST
    # -------------------------------------------------------
    def teardown(self):
        print("\n" + "="*70)
        print("FIN DU TEST - RÉCAPITULATIF")
        print("="*70)
        print(f"Tests réussis : {self.tests_passed}")
        print(f"Tests échoués : {self.tests_failed}")
        print(f"Bugs détectés : {self.bugs_found}")
        print("\nFermeture du navigateur…")
        self.driver.quit()


# -------------------------------------------------------
# Exécution du script
# -------------------------------------------------------
test = TestHideShow()
test.setup()
test.test_01_initial_state_visible()
test.test_02_hide_element()
test.test_03_show_element()
test.test_04_hide_toggle_bug()
test.test_05_show_toggle_bug()
test.test_06_fast_switch()
test.teardown()
