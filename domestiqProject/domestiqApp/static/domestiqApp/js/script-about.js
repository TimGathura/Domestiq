// Get Started button link
document.addEventListener('DOMContentLoaded', function () {
    // Get the button element
    const getStartedButton = document.querySelector('.get-started-btn');

    // Add click event listener to the button
    getStartedButton.addEventListener('click', function () {
        // Redirect to the get-started.html page
        window.location.href = '../html/get-started.html';
    });
});


//Log In button link
document.addEventListener('DOMContentLoaded', function() {
    //Get the log in button element
    const logInButton = document.querySelector('.log-in-btn');

    //Add click event listener to the button
    logInButton.addEventListener('click', function() {
        //Redirect to the log-in.html page
        window.location.href = '../html/log-in.html';
    });
});