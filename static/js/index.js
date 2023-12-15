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

console.log('Script loaded');
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('employeeForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevents the form from submitting by default

        // Perform validation
        if (validateForm()) {
            form.submit(); // If validation passes, submit the form
        }
    });

    function validateForm() {
        console.log("Validation started...");
        const nameInput = document.getElementById('id_name');
        const emailInput = document.getElementById('id_email');
        const addressInput = document.getElementById('id_address');
        const genderInput = document.getElementById('id_gender');
        const phoneNumberInput = document.getElementById('id_phone_number');
        const salaryInput = document.getElementById('id_salary');
        const birthDateInput = document.getElementById('id_birth_date');

        // Validate Name
        const name = nameInput.value.trim();
        if (name === '') {
            alert('Please enter a name');
            return false;
        }
        const nameRegex = /^[A-Za-z\s]+$/;
        if (!nameRegex.test(name)) {
            alert('Name should contain only letters');
            return false;
        }

        // Validate Email
        const email = emailInput.value.trim();
        if (email === '') {
            alert('Please enter an email address');
            return false;
        }
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address');
            return false;
        }

        // Validate Address
        const address = addressInput.value.trim();
        if (address === '') {
            alert('Please enter an address');
            return false;
        }

        // Validate Gender
        const gender = genderInput.value;
        if (gender === '') {
            alert('Please select a gender');
            return false;
        }

        // Validate Phone Number
        const phoneNumber = phoneNumberInput.value.trim();
        if (phoneNumber === '') {
            alert('Please enter a phone number');
            return false;
        }
        // Add specific phone number format validation if needed

        // Validate Salary
        const salary = salaryInput.value.trim();
        if (salary === '') {
            alert('Please enter a salary');
            return false;
        }
        if (isNaN(salary) || parseFloat(salary) <= 0) {
            alert('Please enter a valid salary');
            return false;
        }

        // Validate Birth Date
        const birthDate = birthDateInput.value.trim();
        if (birthDate === '') {
            alert('Please enter a birth date');
            return false;
        }
        // Apply date format validation as previously shown

        return true; // All validation passed    
    }
});

