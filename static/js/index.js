document.addEventListener('DOMContentLoaded', function() {
    const tryButton = document.getElementById('tryButton');

    // Add event listener to the button
    tryButton.addEventListener('click', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Replace 'your-redirect-url' with the actual URL of the page you want to redirect to
        const redirectUrl = 'humanrsc/';

        // Redirect to the specified URL when the button is clicked
        window.location.href = redirectUrl;
    });
});
