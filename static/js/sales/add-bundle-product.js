$('#add-bundle-product').on('submit', function () {
    var bundleId = $("#bundle_id").val();
    var stockId = $("#stock_id").val();
    var bundleProdStatus = $("#bundleprod_status").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/sales/bundleProduct/',

        data: JSON.stringify({
            "data": {
                "type": "BundleProducts",
                "id": null,
                "attributes": {
                    "status": bundleProdStatus,
                    "bundle":"/api/sales/bundle/"+ bundleId+"/",
                    "stock": "/api/inventory/stock/"+ stockId+"/"
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

