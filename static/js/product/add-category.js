$('#add-category').on('submit', function () {
    var categoryName = $("#category_name").val();
    var categoryDescription = $("#category_des").val();
    var parentId = $("#parent_id").val();
    var categoryStatus = $("#category_status").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':getCookie('csrftoken'),
            'sessionid':getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/inventory/category/',

        data: JSON.stringify({
            "data": {
                "type": "Category",
                "id": null,
                "attributes": {
                    "category_name": categoryName,
                    "parent_id": parentId,
                    "category_description": categoryDescription,
                    "status": categoryStatus
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

