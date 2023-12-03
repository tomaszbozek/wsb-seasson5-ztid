// get form fields and error message field
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

// add event listener that is triggered on click event
loginButton.addEventListener("click", (e) => {
    // prevent the default form submission
    e.preventDefault();
    // get username & password values from form fields
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // login guest user
    if (username === "" && password === "") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
