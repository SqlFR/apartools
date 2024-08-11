// Désactive bouton après le clic
function disabledButtonAfterClick() {
    const btnAddIssue = document.getElementById('btn-add-issue');
    setTimeout(() => {
        btnAddIssue.disabled = true;
    }, 10)

    setTimeout(() => {
        btnAddIssue.disabled = false;
    }, 1000);
}
