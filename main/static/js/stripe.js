var stripe = Stripe('pk_test_WSMHaOkBZMUYsHyaNDDEsLGD00wJHHzet3');
var elements = stripe.elements();

var style = {
    base: {
        fontSize: '16px',
        color: '#32325d',
    }
};

var card = elements.create('card', {style: style});

card.mount('#card-element');
