# 🏦 Loan Risk Prediction

## 📝 Description

Ce projet vise à prédire le risque de crédit client pour l'approbation de prêts en s'appuyant sur des indicateurs financiers et des attributs de profil. Le modèle classifie les clients en deux catégories distinctes :

* **0 : Risque Élevé (High Risk)**
* **1 : Risque Faible (Low Risk)**



---

## ✨ Fonctionnalités Clés

* **Gestion des Valeurs Aberrantes :** Utilisation de la **Winsorisation** (basée sur l'IQR) et du **Robust Scaling** pour traiter les valeurs extrêmes des données financières (Variables A1-A4).
* **Modélisation Avancée :** Implémentation de **Random Forest** pour capturer les relations non-linéaires et maintenir une précision élevée malgré des distributions asymétriques.
* **Prétraitement Robuste :** Transformation et mise à l'échelle des variables pour garantir la stabilité des performances du modèle.

---

## 🛠️ Stack Technique

| Catégorie | Outils |
| --- | --- |
| **Langage** | Python |
| **Analyse de données** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn |
| **Visualisation** | Matplotlib, Seaborn |
| **Interface Web** | Streamlit |

---

## 🚀 Installation et Utilisation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ghazalyjamal41/credit-risk-classification

```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt

```

### 3. Lancer l'application Streamlit

```bash
streamlit run app.py

```

---

## 📂 Structure du Projet

* `app.py` : Application web Streamlit pour tester le modèle de manière interactive.
* `Projets Machine Learning.ipynb` : Notebook principal (EDA, gestion des outliers et entraînement).
* `model.pkl` : Modèle entraîné exporté via Pickle.
* `Risque_data.xlsx` : Jeu de données financières brutes.
* `requirements.txt` : Liste des dépendances Python.
* `LICENSE` : Licence MIT.

---
