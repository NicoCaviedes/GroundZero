const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    document.title = "Register - GroundZero";
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    document.title = "Login - GroundZero";
	container.classList.remove("right-panel-active");
});