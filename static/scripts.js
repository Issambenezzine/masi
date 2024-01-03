function submitForm() {
    // Récupérer les données du formulaire
    var seance = $('#seance').val();
    var cours_cloture = $('#cours_cloture').val();
    var cours_ouverture = $('#cours_ouverture').val();
    var volume_jj = $('#volume_jj').val();
    var indice_monia = $('#indice_monia').val();
    var encours = $('#encours').val();

    // Envoyer les données au serveur pour la prédiction
    $.post('/predict', {
        seance: seance,
        cours_cloture: cours_cloture,
        cours_ouverture: cours_ouverture,
        volume_jj: volume_jj,
        indice_monia: indice_monia,
        encours: encours
    }, function (data) {
        // Afficher le résultat de la prédiction
        $('#predictionResult').text(data);
        $('#result').removeClass('hidden');
    });
}
