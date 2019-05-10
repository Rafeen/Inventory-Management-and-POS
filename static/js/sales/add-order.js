$('#add-order').on('submit', function () {
    var orderId = $("#order_id").val();
    var orderClient = $("#order_client").val();
    var orderType = $("#order_type").val();
    var orderStatus = $("#order_status").val();
    var createdBy = $("#creator").val();
    var orderDate = $("#order_date").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/sales/order/',

        data: JSON.stringify({
            "data": {
                "type": "Order",
                "id": null,
                "attributes": {
                    "order_id": orderId,
                    "order_type": orderType,
                    "status": orderStatus,
                    "created_by": createdBy,
                    "order_date": orderDate,
                     "client": "/api/sales/clients/"+orderClient+"/",

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

