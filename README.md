# datalogger1
debut d'une architecture test
# Mini Home Assistant

Une version ultra-simplifiée de Home Assistant pour comprendre les concepts de base :
- Backend en Python (Flask)
- Capteurs simulés
- Base de données SQLite
- Interface Web simple

## 💡 Fonctionnalités

- Simulation d'un capteur de température
- Affichage en temps réel
- Commande d'une lumière virtuelle

## 🛠️ Installation

```bash
pip install -r requirements.txt
python init_db.py
python app.py

Accède à l'interface via http://localhost:5000


✅ Fonctionnalités implémentées
Simule un capteur de température toutes les 5 secondes.
Stocke les mesures dans une base SQLite.
Affiche la dernière valeur sur une page web.
Possibilité d’allumer une lampe virtuelle via une requête POST.