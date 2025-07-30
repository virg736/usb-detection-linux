# usb-detection-linux
Projet pédagogique pour détecter et surveiller les clés USB sous Linux  ( kali, Virtualbox).


🔍 Sommaire
	1.	Objectif du projet
	2.	Pourquoi la sécurité USB est essentielle
	3.	À qui s’adresse ce projet
	4.	Niveaux du projet
	•	Niveau débutant
	•	Niveau intermédiaire
	•	Niveau expert
	5.	Différence entre simulation et clé réelle
	6.	Captures d’écran
	7.	Utilisation des scripts
	8.	Licence

⸻

🎯 Objectif du projet

Ce projet a pour but de détecter et surveiller les périphériques USB sur un système Linux. Il est structuré en trois niveaux de difficulté, pour permettre une progression pédagogique :
	•	🔹 Lister les périphériques USB connectés
	•	🔹 Simuler une clé USB pour tester la logique de détection
	•	🔹 Détecter en temps réel une clé USB physique à l’aide d’événements matériels

Testé sur : Kali Linux sous VirtualBox

⸻

🔐 Pourquoi la sécurité USB est essentielle

Les périphériques USB sont des vecteurs d’attaque fréquents :
	•	⚠️ Introduction de malwares (clés infectées)
	•	📤 Vol de données sensibles
	•	🧨 Attaques physiques déguisées (ex: BadUSB)
	•	🚫 Intrusions dans des environnements critiques

Surveiller les connexions USB est donc essentiel, notamment dans des environnements sensibles ou professionnels.

⸻

👤 À qui s’adresse ce projet