#!/bin/bash

echo "🔌 Liste des périphériques USB connectés :"
lsusb

echo ""
echo "💾 Périphériques de stockage montés :"
lsblk -o NAME,MOUNTPOINT,SIZE,FSTYPE

echo ""
echo "🔐 Droits d'accès sur les périphériques :"
ls -l /dev/sd*
