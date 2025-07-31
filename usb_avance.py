## 🔍 usb_detector.py — Détection avancée (niveau expert)

Ce script Python utilise la bibliothèque `pyudev` pour surveiller en temps réel les connexions de périphériques USB physiques.

### Fonctionnalités :
- Détection en direct d’une clé USB insérée (`device.action == 'add'`)
- Identification du nom du périphérique
- Lecture du contenu si le périphérique est monté
- Affichage d’un message si la clé est détectée mais non montée

📌 **Remarque :** Ce script **nécessite une clé USB réelle branchée**.  
Il **ne peut pas être testé** dans un environnement virtualisé ou Check Pass (pas d’accès au matériel physique).

#!/usr/bin/env python3
import pyudev
import os

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block', device_type='partition')

print("🕵️ En attente d’une clé USB... (CTRL+C pour quitter)")

for device in iter(monitor.poll, None):
    if device.action == 'add':
        device_node = device.device_node
        device_name = os.path.basename(device_node)

        mount_point = None
        with open('/proc/mounts', 'r') as f:
            for line in f:
                if device_node in line:
                    mount_point = line.split()[1]
                    break

        if mount_point:
            print(f"\n✅ Clé USB détectée : {device_name}")
            print(f"📂 Contenu de {mount_point} :")
            for root, dirs, files in os.walk(mount_point):
                for file in files:
                    print(f"- {os.path.join(root, file)}")
        else:
            print(f"\n⚠️ Clé détectée ({device_name}) mais non montée.")