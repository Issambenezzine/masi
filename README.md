# Prédiction de l'Indice MASI - Projet Flask

Ce projet est une application Flask qui utilise un modèle préentraîné pour prédire la variation de l'Indice MASI (Moroccan All Shares Index) en fonction des données fournies. L'application propose un formulaire convivial pour saisir les données de prédiction et affiche ensuite le résultat de la prédiction.

## Structure du Projet

- `MASI.py` : Le fichier principal contenant le code de l'application Flask.
- Dossier `templates` :
  - `index.html` : Le formulaire HTML pour collecter les données de prédiction.
- Dossier `static` :
  - `styles.css` : Le fichier CSS pour le style de la page.
  - `scripts.js` : Le script JavaScript pour gérer l'envoi des données de formulaire au serveur.

## Comment Exécuter le Projet

1. **Installer les Dépendances :**
   - Assurez-vous d'avoir Flask installé. Sinon, installez-le en utilisant `pip install Flask`.

2. **Exécuter l'Application :**
   - Exécutez le fichier `MASI.py`.
   - L'application sera disponible sur `http://127.0.0.1:5000/` dans votre navigateur.

## Utilisation de l'Application

1. **Formulaire de Prédiction :**
   - Accédez à l'application en visitant la route principale (`/`).
   - Remplissez les champs du formulaire avec les données nécessaires.
   - Cliquez sur le bouton "Prédire" pour envoyer les données au serveur.

2. **Prédiction :**
   - Les données du formulaire sont envoyées au serveur via une requête POST.
   - Le serveur utilise le modèle préentraîné (`modele_prediction_masi.joblib`) pour faire la prédiction.
   - Le résultat de la prédiction est renvoyé au client.

3. **Affichage du Résultat :**
   - Le résultat de la prédiction est affiché sur la page.

## Conclusion

Cette application offre une interface utilisateur simple et interactive pour interagir avec le modèle de prédiction de l'Indice MASI. Le modèle est entraîné sur des données historiques de l'Indice MASI et peut être utilisé pour faire des prédictions en temps réel. Personnalisez l'application selon vos besoins en modifiant les fichiers HTML, CSS et JavaScript.

---

# Modélisation de l'Indice MASI - Notebook Jupyter

Le fichier Jupyter `IDATECH.ipynb` contient les étapes de modélisation utilisées pour créer le modèle préentraîné. Voici un résumé des étapes :

## 1. Prétraitement des Données

- Chargement des données historiques de l'Indice MASI.
- Exploration des données et gestion des valeurs manquantes.

## 2. Sélection des Fonctionnalités

- Analyse de corrélation pour sélectionner les fonctionnalités les plus importantes.

## 3. Entraînement du Modèle

- Utilisation de XGBoost pour créer un modèle de régression.
- Optimisation des hyperparamètres du modèle.

## 4. Évaluation du Modèle

- Division des données en ensembles d'entraînement et de test.
- Évaluation des performances du modèle sur l'ensemble de test.

## 5. Sauvegarde du Modèle

- Utilisation de Joblib pour sauvegarder le modèle entraîné.

---

**Remarque :** Assurez-vous d'avoir toutes les dépendances nécessaires installées avant d'exécuter le notebook Jupyter. Utilisez `pip install -r requirements.txt` pour installer les dépendances.
