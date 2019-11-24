// JavaScript code from tutorial included in Stripe documentation found at `https://stripe.com/docs/payments/cards/collecting/web`

// Create a Stripe client
var stripe = Stripe('pk_test_WSMHaOkBZMUYsHyaNDDEsLGD00wJHHzet3');

// Create an instance of Stripe Elements
var elements = stripe.elements();

// Add input styles
var style = {
    base: {
        fontSize: '16px',
        fontFamily: '"Questrial", sans-serif',
        color: '#18121E',
    }
};

// Create an instance of the card Element
var card = elements.create('card', {style: style});

// Add instance of card Element into the card-element div
card.mount('#card-element');

// Listen to change events and display errors
card.addEventListener('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Create a token or display an error when the form is submitted
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.createToken(card).then(function(result) {
        if (result.error) {
            // Inform the customer that there was an error
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // Send the token to the server
            stripeTokenHandler(result.token);
        }
    });
});

// Submit the token to the server
function stripeTokenHandler(token) {
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);

    // Submit the form
    form.submit();
}