# Projet de Tests Manuels et Automatisés – Automation Practice

Ce dépôt regroupe l’ensemble du travail de tests réalisé sur le site :

> https://rahulshettyacademy.com/AutomationPractice/

Il s’inscrit dans le cadre du module **Tests Manuels et Automatisés** de la Licence **Business Computing** à l’ESPRIT School of Business.  
Le projet combine :

- une **démarche de test manuel structurée** (plan de test, cas de test, exécution, analyse),
- des **scripts de tests automatisés** développés en **Python/Selenium**,
- une **analyse critique** des résultats et des anomalies détectées.

---

## 1. Objectifs du projet

Les principaux objectifs pédagogiques sont :

- Appliquer une **méthodologie de test professionnelle** (cycle de vie des tests).
- Rédiger un **rapport de tests** clair et structuré (introduction, planification, conception, exécution, analyse).
- Mettre en œuvre des **tests automatisés** avec Selenium WebDriver :
  - interaction avec les éléments d’interface (checkboxes, liens, boutons),
  - validation des comportements attendus,
  - détection d’anomalies fonctionnelles.
- Comparer les apports et les limites :
  - des **tests manuels**,
  - des **tests automatisés**.

---

## 2. Fonctionnalités testées

Deux fonctionnalités principales du site Automation Practice ont été étudiées :

### 2.1. Fonctionnalité « Checkboxes »

Zone de sélection multiple, composée de trois cases à cocher :

- `Option1`
- `Option2`
- `Option3`

Les tests portent notamment sur :

- la **sélection / désélection** individuelle de chaque checkbox ;
- la possibilité de **cocher plusieurs cases simultanément** ;
- la cohérence de l’état affiché par le navigateur après chaque action.

### 2.2. Fonctionnalité « Social Media »

Section située en bas de page, présentant les libellés :

- `Facebook`
- `Twitter`
- `Google+`
- `Youtube`

Les tests visent à vérifier que chaque élément :

- est implémenté comme un **lien cliquable** (`<a>` avec attribut `href`) ;
- redirige correctement l’utilisateur (ou ouvre un nouvel onglet) vers le réseau social attendu ;
- respecte les bonnes pratiques d’ergonomie et de navigation.

---

## 3. Contenu du dépôt

- `Rapport_de_Tests_Manuels_et_Automatisés.pdf`  
  Rapport complet incluant :
  - description du site et des fonctionnalités ;
  - stratégie de test et périmètre ;
  - cas de tests détaillés (tests manuels) ;
  - résultats, anomalies, propositions d’amélioration ;
  - introduction aux scripts de tests automatisés.

- `test_checkbox.py`  
  Script d’automatisation des tests sur la fonctionnalité **Checkboxes** :
  - ouverture du navigateur et accès à la page Automation Practice ;
  - sélection puis désélection de chaque checkbox ;
  - vérification de l’état avec `is_selected()` après chaque action ;
  - scénario global avec les **trois cases cochées** pour valider la tolérance multi-sélection.

- `test_social_media.py`  
  Script d’automatisation des tests sur la section **Social Media** :
  - défilement de la page jusqu’à la zone des réseaux sociaux ;
  - recherche des libellés `Facebook`, `Twitter`, `Google+`, `Youtube` ;
  - contrôle de la nature de l’élément HTML (lien `<a>` ou texte statique) ;
  - vérification de l’existence d’un `href` et de l’ouverture d’un nouvel onglet ;
  - affichage d’un résumé et signalement des anomalies en console (et éventuelle alerte dans le navigateur).

---

## 4. Environnement technique

- **Langage** : Python 3
- **Framework d’automatisation** : Selenium WebDriver
- **Gestionnaire de driver** : `webdriver-manager` (pour le driver Chrome)
- **Navigateur ciblé** : Google Chrome
- **IDE / Éditeur** : Visual Studio Code (ou équivalent)
- **Système d’exploitation** : Windows 10

---

## 5. Prérequis

Avant d’exécuter les scripts, installer les dépendances suivantes :

```bash
pip install selenium webdriver-manager
