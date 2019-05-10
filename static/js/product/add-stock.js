$('#add-stock').on('submit', function () {
    var stockBatchNumber = $("#batch_number").val();
    var purchasePrice = $("#purchase_price").val();
    var purchaseTax = $("#purchase_tax").val();
    var stockStatus =$("#stock_status").val();
    var stockQuantity =$("#stock_quantity").val();
    var stockSku =$("#stock_sku").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/inventory/stock/',

        data: JSON.stringify({
            "data": {
                "type": "Stock",
                "id": null,
                "attributes": {
                    "stock_quantity": stockQuantity,
                    "batch_number": stockBatchNumber,
                    "purchase_price": purchasePrice,
                    "purchase_tax": purchaseTax,
                    "barcode": stockSku,
                    "status": stockStatus,
                    "sku":"/api/inventory/product/"+stockSku+"/",
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