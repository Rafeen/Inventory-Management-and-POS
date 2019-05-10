$('#add-warehouse').on('submit', function () {

    var warehouseName = $("#wh_name").val();
    var  warehouseAddress = $("#wh_address").val();
    var  warehouseCity = $("#wh_city").val();
    var  warehousePhone = $("#wh_phone").val();
    var  warehouseCountry = $("#wh_country").val();
    var  warehouseType = $("#wh_type").val();
    var  warehouseStatus = $("#wh_status").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/inventory/warehouse/',

        data: JSON.stringify({
            "data": {
                "type": "Warehouse",
                "id": null,
                "attributes": {
                    "wh_name": warehouseName,
                    "wh_address": warehouseAddress,
                    "wh_city": warehouseCity,
                    "wh_country": warehouseCountry,
                    "wh_phone": warehousePhone,
                    "wh_status": warehouseStatus,
                    "wh_type": warehouseType,

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

