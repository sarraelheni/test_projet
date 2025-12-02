# Projet Final – Test Logiciel Manuel

## Groupe
- Testeur : Hanine Ben Ahmed
- Site choisi : [Rahul Shetty Automation Practice](https://rahulshettyacademy.com/AutomationPractice/)
- Fonctionnalité testée : Switch to Alert Example
- Date du test : 18 Novembre 2025
- Type de test : Manuel / Fonctionnel
- Navigateur : Google Chrome 119.0
- Système d’exploitation : Windows 10
- Version du rapport : 1.0

---

## I. Objectif
L'objectif de ce projet est de réaliser un test manuel sur la fonctionnalité "Switch to Alert" pour vérifier la gestion des alertes JavaScript dans le site web choisi.

---

## II. Périmètre du test
La fonctionnalité testée couvre :
1. Champ **Enter Your Name** : saisie de texte.
2. Bouton **Alert** : affichage de l’alerte, lecture du message, clic sur OK.
3. Bouton **Confirm** : affichage de l’alerte de confirmation, lecture du message et validation des deux actions possibles (OK / Cancel).

---

## III. Plan de test

| ID Test | Objectif | Préconditions | Étapes d’exécution | Résultat attendu | Résultat obtenu | Statut |
|---------|----------|---------------|------------------|-----------------|----------------|--------|
| CT-01   | Affichage de l’alerte | Page ouverte, bouton visible | Cliquer sur "Click for JS Alert" | Alerte affichée | Alerte affichée | PASS |
| CT-02   | Vérification du message | Alerte affichée | Lire le texte de l’alerte | "This is a JavaScript Alert" | "This is a JavaScript Alert" | PASS |
| CT-03   | Test du bouton OK | Alerte affichée, bouton OK visible | Cliquer sur OK | Alerte se ferme, page interactive | Alerte se ferme, page interactive | PASS |
| CT-04   | Message après fermeture | Alerte fermée | Observer la page | Message : "You successfully clicked an alert" | Aucun message affiché | FAIL |

**Statistiques :**
- Nombre total de cas de test : 4
- Tests réussis (PASS) : 3
- Tests échoués (FAIL) : 1
- Taux de réussite : 75%
- Durée totale des tests : 2 minutes

---

## IV. Rapport d’anomalie

**Bug ID** : BUG-001  
**Titre** : Message après fermeture de l’alerte non affiché  
**Description** : Après avoir cliqué sur le bouton Alert et validé l’alerte avec OK, le message attendu `"You successfully clicked an alert"` ne s’affiche pas sur la page.  
**Gravité** : Élevée  
**Priorité** : Moyenne  
**État** : Ouvert  
**Étapes pour reproduire** :
1. Accéder à la page AutomationPractice  
2. Saisir un nom dans le champ Enter Your Name  
3. Cliquer sur Alert  
4. Cliquer sur OK dans l’alerte

---

## V. Observations et recommandations
- Corriger le script JavaScript pour afficher correctement le message après la fermeture de l’alerte.  
- Ajouter un test de validation post-alerte dans le cycle de test.  
- Vérifier la compatibilité sur différents navigateurs (Chrome, Firefox, Edge).

---

## VI. Annexes
- Captures d’écran prises pendant les tests (voir dossier `screenshots/` si disponible).  
- Environnement de test : Windows 10, Chrome 119.0, résolution 1920x1080.  

---

**Fin du rapport – Document conforme aux standards de test logiciel**  
Réalisé par : Hanine Ben Ahmed
