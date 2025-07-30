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

**Script : `usb_devices_info.sh`**

bash
#!/bin/bash

echo "Liste des périphériques USB connectés :"
lsusb

echo -e "\nPériphériques montés :"
lsblk

echo -e "\nPermissions sur les périphériques :"
ls -l /dev/sd*







