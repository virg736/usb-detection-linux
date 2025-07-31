#!/usr/bin/env python3
"""
usb_detector.py - Détection en temps réel d'une clé USB physique sous Linux

Ce script pédagogique utilise la bibliothèque `pyudev` pour détecter automatiquement
l'insertion d'une clé USB. Il affiche le nom du périphérique, son point de montage
(et son contenu s'il est monté).

⚠️ Usage pédagogique uniquement. Aucune responsabilité en cas de modification,
utilisation en production ou redistribution. Licence : MIT.
"""

import os
import pyudev
from datetime import datetime

# Initialisation du système de surveillance udev
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block', device_type='partition')

print("🟢 En attente d'une clé USB... (CTRL+C pour quitter)")

try:
for device in iter(monitor.poll, None):
if device.action != 'add':
continue

device_node = device.device_node
device_name = os.path.basename(device_node)
mount_point = None

# Vérifie si le périphérique est monté
with open("/proc/mounts", 'r') as f:
for line in f:
if device_node in line:
mount_point = line.split()[1]
break

# Affiche les infos
print(f"\n🕒 {datetime.now()} - Clé USB détectée : {device_name}")
if mount_point:
print(f"📂 Montée sur : {mount_point}")
print("📁 Contenu :")
for root, dirs, files in os.walk(mount_point):
for file in files:
print(f" - {os.path.join(root, file)}")
else:
print(f"⚠️ Clé détectée ({device_name}) mais non montée.")
except KeyboardInterrupt:
print("\n🛑 Surveillance arrêtée par l'utilisateur.")
