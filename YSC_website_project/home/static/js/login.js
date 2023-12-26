
// Login
function preventScroll(e) {
    e.preventDefault();
    e.stopPropagation();

    return false;
}

function showLogin() {
    document.querySelector(".login-popup-container").classList.add("active");
    // Disable scrollwheel until pressed out of
    document.querySelector(".login-popup-container").addEventListener('mousewheel', preventScroll);
}

function closeLogin() {
    document.querySelector(".login-popup-container").classList.remove("active");
}
  
document.getElementById("show-login").addEventListener("click", showLogin)
document.querySelector(".login-popup .close-btn").addEventListener("click", closeLogin)