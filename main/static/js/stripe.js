$(function() {
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvc").val()
        };
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#card-errors").hide();
            $("#id_stripe_id").val(response.id);

            // Prevent the Credit Card Details from being submitted to our server
            $("#id_card_number").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');
            $("#id_cvc").removeAttr('name');

            form.submit();
        } else {
            $("#stripe-error-message").text(response.error.message);
            $("#card-errors").show();
            $("#validate_card_btn").atrr("disabled", false);
        }
    });
    return false;
    });
});