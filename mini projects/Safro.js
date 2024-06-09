document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    // Simple form validation
    if (name && email && message) {
        // Here you can add code to send the form data to your server
        console.log('Form submitted:', { name, email, message });
        alert('Thank you for your message, ' + name + '!');
        document.getElementById('contact-form').reset();
    } else {
        alert('Please fill out all fields.');
    }
});
