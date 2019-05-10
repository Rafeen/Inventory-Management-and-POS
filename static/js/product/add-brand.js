$('#add-brand').on('submit', function () {
    var brandName = $("#brand_name").val();
    var brandDescription = $("#brand_des").val();
    var brandStatus = $("#brand_status").val();
    alert(brandName);
    alert(brandDescription);
    alert(brandStatus);

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/inventory/brand/',

        data: JSON.stringify({
            "data": {
                "type": "Brand",
                "id": null,
                "attributes": {
                    "brand_name": brandName,
                    "brand_description": brandDescription,
                    "status": brandStatus
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