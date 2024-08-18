// Désactive bouton ajouter incident après le clic
function disabledButtonAfterClick() {
    const btn = document.querySelector('.btn');
    setTimeout(() => {
        btn.disabled = true;
    }, 10)

    setTimeout(() => {
        btn.disabled = false;
    }, 1000);
}

// Gère la flèche sous le bouton Ajouter incidents et le changement du texte

// Récupère le texte du bouton pour le retourner après la réduction du slide
const button_to_slide = document.querySelector('.btn-open-slide-form')
const initial_text_button = button_to_slide.querySelector('span').textContent;

function toggleForm(button) {
    let formContainer = document.querySelector('.contain-slide-form');

    setTimeout(() => {
        button.disabled = true;
    }, 10)

    setTimeout(() => {
        button.disabled = false;

    }, 1000);
    if (formContainer.style.display === 'block') {
        formContainer.style.display = 'none';
        button.querySelector('span').textContent = initial_text_button;
        button.setAttribute('aria-expanded', 'false');

    } else {
        formContainer.style.display = 'block';
        button.querySelector('span').textContent = 'Réduire';
        button.setAttribute('aria-expanded', 'true');
    }
}