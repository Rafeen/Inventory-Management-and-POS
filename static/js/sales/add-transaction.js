$('#add-transaction').on('submit', function () {
    var paidAmount = $("#pay_amount").val();
    var payMethod = $("#payment_type").val();
    var tranDate = $("#transaction_date").val();
    var tranStatus = $("#transaction_status").val();
    var createdBy = $("#creator").val();
    var orderID = $("#order_id").val();

    alert(paidAmount);
    alert(payMethod);
    alert(tranDate);
    alert(tranStatus);
    alert(createdBy);
    alert(orderID);

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/sales/transaction/',

        data: JSON.stringify({
            "data": {
                "type": "Transactions",
                "id": null,
                "attributes": {
                    "paid_amount": paidAmount,
                    "payment_method": payMethod,
                    "transaction_date": tranDate,
                    "status": tranStatus,
                    "created_by": createdBy,
                    "order":'/api/sales/order/'+orderID+"/",
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

