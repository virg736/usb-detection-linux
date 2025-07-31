#!/usr/bin/env python3
import os
import time

USB_PATH = "/media/usb_simulation"

def check_usb():
    return os.path.ismount(USB_PATH) or os.path.exists(USB_PATH)

print("✅ Surveillance de la 'clé USB simulée'... (Ctrl+C pour quitter)")

already_present = check_usb()

try:
    while True:
        current_state = check_usb()
        if current_state != already_present:
            if current_state:
                print("✅ Clé USB simulée détectée !")
            else:
                print("❌ Clé USB simulée retirée.")
            already_present = current_state
        time.sleep(2)
except KeyboardInterrupt:
    print("\n🛑 Surveillance arrêtée.")
