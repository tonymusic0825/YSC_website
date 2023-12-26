console.log("app.js connected")

var profile_clicked = false

// Click profile
function openUserContent() {
  console.log('Clicked user-logo')
  if (!profile_clicked) {
    document.querySelector(".user-content").classList.add("active");
    profile_clicked = true;
  } else {
    document.querySelector(".user-content").classList.remove("active");
    profile_clicked = false;
  }
}

document.querySelector("#user-logo").addEventListener("click", openUserContent)

// Close alert
function closeAlert() {
  document.querySelector(".alert").classList.add("close");
}

document.querySelector(".close-alert").addEventListener("click", closeAlert)

// Date for footer
const date = document.getElementById("date")
const currentYear = new Date().getFullYear()
date.textContent = currentYear

