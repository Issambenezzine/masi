from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Charger le modèle préentraîné
modele_prediction_masi = joblib.load('modele_prediction_masi.joblib')

# Route pour afficher le formulaire
@app.route('/')
def formulaire():
    return render_template('index.html')

# Route pour traiter la prédiction
@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        seance = pd.to_datetime(request.form['seance']).timestamp()
        cours_cloture = float(request.form['cours_cloture'])
        cours_ouverture = float(request.form['cours_ouverture'])
        volume_jj = float(request.form['volume_jj'])
        indice_monia = float(request.form['indice_monia'])
        encours = float(request.form['encours'])

        # Créer un DataFrame avec les données du formulaire
        donnees_formulaire = pd.DataFrame({
            'SEANCE': [seance],
            'COURS_CLOTURE': [cours_cloture],
            'COURS_OUVERTURE': [cours_ouverture],
            'Volume JJ': [volume_jj],
            'Indice MONIA': [indice_monia],
            'ENCOURS': [encours]
        })

        # Faire la prédiction avec le modèle
        prediction_variation = modele_prediction_masi.predict(donnees_formulaire)

        # Afficher le résultat
        return f"Prédiction de la variation : {prediction_variation[0]}"

if __name__ == '__main__':
    app.run(debug=True)
