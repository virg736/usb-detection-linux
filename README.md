#  Détection et Surveillance des Clés USB sous Linux
## Sommaire

- [Objectif du projet](#objectif-du-projet)
- [Pourquoi la sécurité USB est essentielle](#pourquoi-la-sécurité-usb-est-essentielle)
- [À qui s’adresse ce projet](#à-qui-sadresse-ce-projet)
- [Niveaux du projet](#niveaux-du-projet)
- [Niveau débutant](#niveau-débutant)
- [Niveau intermédiaire](#niveau-intermédiaire)
- [Niveau expert](#niveau-expert)
- [Différence entre simulation et clé réelle](#différence-entre-simulation-et-clé-réelle)
- [Captures d’écran](#captures-décran)
- [Utilisation des scripts](#utilisation-des-scripts)
- [Licence](#licence)

---

## Objectif du projet

Ce projet a pour but de détecter et surveiller les périphériques USB sur un système Linux.
Il est structuré en trois niveaux de difficulté, permettant une montée progressive en compétence :

- Lister les périphériques USB connectés
- Simuler une clé USB pour tester la logique de détection
- Détecter automatiquement une clé USB réelle en temps réel

> Ce projet est conçu à des fins pédagogiques et a été testé dans un environnement **Kali Linux sous VirtualBox**.

---

## Pourquoi la sécurité USB est essentielle

Les clés USB sont souvent utilisées comme vecteurs d’attaque :

- Introduction de malwares (clé infectée)
- Vol de données
- Attaques physiques via périphériques déguisés (BadUSB)
- Intrusion non autorisée dans des environnements sensibles

Il est donc **essentiel de surveiller et détecter** tout périphérique USB connecté à une machine, en particulier sur les postes critiques.

---

## À qui s’adresse ce projet

### Public visé & Objectifs pédagogiques

| Public | Objectifs |
|---------------------------|-----------|
| **Étudiants en cybersécurité** | Comprendre les risques USB et créer ses premiers scripts |
| **Formateurs / enseignants** | Appui pour travaux pratiques gradués (TP) |
| **Administrateurs système** | Surveiller les postes sensibles pour des connexions USB |
| **Pentesters / pros sécurité** | Démontrer les vecteurs d’intrusion physiques |

---

## Niveaux du projet

### Niveau débutant

**Objectif** : Identifier les périphériques USB connectés via des commandes de base.

**Script :** `usb_devices_info.sh`

bash
#!/bin/bash

echo "Liste des périphériques USB connectés :"
lsusb

echo -e "\nPériphériques montés :"
lsblk

📸 Captures d’écran :

![Contenu du script `usb_devices_info.sh`](securite2.PNG)
*Affichage du script dans Nano*


![Résultat du script `usb_devices_info.sh`](secure3.PNG)
*Exécution dans le terminal sous Kali Linux*

---

### Niveau intermédiaire

**Objectif** : Simuler l’insertion d’une clé USB en utilisant un dossier comme point de montage.

Ce niveau permet de tester la logique de détection **sans clé USB physique**, en créant une **clé USB virtuelle** (simple dossier).

---

###  Étapes réalisées

1. Création d’un dossier simulant une clé USB :
bash
mkdir -p /media/usb_simulation
touch /media/usb_simulation/test_usb.txt

Création du script simulate_usb.py :

import os
import time

usb_path = "/media/usb_simulation"

print("Surveillance de la 'clé USB simulée'... (Ctrl+C pour quitter)")
while True:
if os.path.exists(usb_path):
print("Clé USB simulée détectée !")
break
time.sleep(1)

chmod +x simulate_usb.py
./simulate_usb.py

---

**"J'ai créé une clé USB virtuelle, un script de détection, et je l'ai testé dans le terminal."**

### 📸 Captures d’écran

![Création du dossier simulant une clé USB](securite6.PNG) 
*Dossier `/media/usb_simulation` et fichier `test_usb.txt` créés pour simuler une clé USB*

![Écriture du script `simulate_usb.py`](securite4.PNG) 
*Script Python qui surveille l'existence de la "clé USB simulée"*

![Exécution du script `simulate_usb.py`](securite5.PNG) 
*La clé USB simulée est détectée avec succès par le script*


---

Niveau expert

Objectif : Détecter en temps réel l’insertion d’une vraie clé USB à l’aide de la bibliothèque pyudev.


Script : usb_detector.py

📸 Captures associées : secure8.PNG, secure9.PNG

---

Différence entre simulation et clé réelle 
Critère

Intermédiaire

Expert



Captures d’écran


Les captures se trouvent dans le dossier /captures/ du projet :

secure3.PNG – Affichage des périphériques (débutant)

securite4.PNG, securite5.PNG, securescript.PNG – Simulation clé USB (intermédiaire)

secure8.PNG, secure9.PNG – Détection réelle (expert)

Utilisation des scripts


Prérequis
Python 3 installé

Installer pyudev pour le niveau expert :

pip install pyudev

Lancer les scripts
# Débutant
bash usb_devices_info.sh

# Intermédiaire
python3 simulate_usb.py

# Expert
python3 usb_detector.p

# Débutant
bash usb_devices_info.sh

# Intermédiaire
python3 simulate_usb.py

# Expert
python3 usb_detector.py


Licence


Projet libre pour usage pédagogique, personnel ou en formation.

Aucune responsabilité n’est engagée en cas d’utilisation en environnement professionnel sans validation sécurité







