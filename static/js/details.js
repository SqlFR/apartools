// Désactive bouton ajouter incident après le clic
function disabledButtonAfterClick() {
    const btnAddIssue = document.getElementById('btn-add-issue');
    setTimeout(() => {
        btnAddIssue.disabled = true;
    }, 10)

    setTimeout(() => {
        btnAddIssue.disabled = false;
    }, 1000);
}

// Gère la flèche sous le bouton Ajouter incidents et le changement du texte
function toggleForm(button) {
    let formContainer = document.getElementById('contain-form-add-issue');
    setTimeout(() => {
        button.disabled = true;
    }, 10)

    setTimeout(() => {
        button.disabled = false;

    }, 1000);
    if (formContainer.style.display === 'block') {
        formContainer.style.display = 'none';
        button.querySelector('span').textContent = 'Ajouter incidents';
        button.setAttribute('aria-expanded', 'false');

    } else {
        formContainer.style.display = 'block';
        button.querySelector('span').textContent = 'Réduire';
        button.setAttribute('aria-expanded', 'true');
    }
}


// Ajoute class label-input a la div qui contient label/input ds le form add issue et add apart
