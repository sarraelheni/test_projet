# SwitchToAlertTest

## Description
Ce projet contient un script d’automatisation de tests pour le site **Rahul Shetty Academy – AutomationPractice**.  
Le script teste les fonctionnalités d’alertes (alerte simple et alerte de confirmation) en utilisant **Selenium WebDriver (Python)**.

## Fonctionnalités testées
1. **Alerte simple**  
   - Vérifie le message affiché.  
   - Accepte l’alerte.

2. **Alerte de confirmation**  
   - Vérifie le message affiché.  
   - Accepte (OK) et refuse (Cancel) l’alerte.

## Points forts du script
- **Assertions** : valident automatiquement que les messages affichés sont corrects.  
- **Gestion des erreurs** : capture les alertes manquantes ou messages incorrects.  
- **Captures d’écran** : générées automatiquement en cas d’échec pour faciliter le débogage.  
- **Fichier de log** : enregistre tous les résultats de test et captures associées avec timestamp.  
- **Robuste et structuré** : utilisation de `WebDriverWait` pour attendre les alertes dynamiquement.  

## Structure du projet
SwitchToAlertTest/
│
├─ scripts/
│ └─ test_switch_alert.py # Script principal d'automatisation
├─ screenshots/ # Captures d’écran générées automatiquement
├─ test_log.txt # Log des résultats
├─ chromedriver.exe # WebDriver pour Chrome
└─ README.md # Ce fichier

## Prérequis
- Python 3.x
- Selenium (`pip install selenium`)
- Chrome et **chromedriver** compatible

