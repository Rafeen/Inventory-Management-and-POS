$('#add-bundle').on('submit', function () {
    var bundleName = $("#bundle_name").val();
    var bundleDescription = $("#bundle_des").val();
    var bundleStatus = $("#bundle_status").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/sales/bundle/',

        data: JSON.stringify({
            "data": {
                "type": "Bundle",
                "id": null,
                "attributes": {
                    "bundle_name": bundleName,
                    "bundle_description": bundleDescription,
                    "status": bundleStatus
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

