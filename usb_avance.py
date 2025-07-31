## 🔍 usb_detector.py — Détection avancée (niveau expert)

Ce script Python utilise la bibliothèque `pyudev` pour surveiller en temps réel les connexions de périphériques USB physiques.

### Fonctionnalités :
- Détection en direct d’une clé USB insérée (`device.action == 'add'`)
- Identification du nom du périphérique
- Lecture du contenu si le périphérique est monté
- Affichage d’un message si la clé est détectée mais non montée

📌 **Remarque :** Ce script **nécessite une clé USB réelle branchée**.  
Il **ne peut pas être testé** dans un environnement virtualisé ou Check Pass (pas d’accès au matériel physique).
