$('#add-client').on('submit', function () {
    var clientName = $("#client_name").val();
    var clientDescription = $("#client_description").val();
    var clientEmail = $("#client_email").val();
    var clientPhone = $("#client_phone").val();
    var clientAddress = $("#client_address").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/sales/clients/',

        data: JSON.stringify({
            "data": {
                "type": "Clients",
                "id": null,
                "attributes": {
                    "client_name": clientName,
                    "client_description": clientDescription,
                    "client_address": clientAddress,
                    "client_email": clientEmail,
                    "client_phone": clientPhone

                }
            }
        }),

        success: function (status) {
            console.log(status);
        },
        error: function (xhr, textStatus, error) {
            console.log(xhr.responseText);
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }

    });
});

