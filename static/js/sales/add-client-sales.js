$('#add-client-sales').on('submit', function () {
    var stockId = $("#stock_id").val();
    var client = $("#clients").val();
    var warehouse = $("#warehouse").val();
    var quantity = $("#quantity").val();
    var saleDate = $("#date").val();



    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/sales/clientSales/',

        data: JSON.stringify({
            "data": {
                "type": "ClientSales",
                "id": null,
                "attributes": {
                    "quantity": quantity,
                    "sales_date": saleDate,
                    "sku":"/api/inventory/stock/"+stockId+"/",
                    "client": "/api/sales/clients/"+client+"/",
                    "warehouse": "/api/inventory/warehouse/"+warehouse+"/",
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

