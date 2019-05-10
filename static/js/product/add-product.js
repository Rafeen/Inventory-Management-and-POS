$('#add-product').on('submit', function () {
    var p_name = $("#p_name").val();
    var sku = $("#sku").val();
    var brand_id = $("#brand_id").val();
    var category_id = $("#category_id").val();
    var pro_pr = $("#pro_pr").val();
    var pro_tax = $("#pro_tax").val();
    var pro_des = $("#pro_des").val();
    var pro_color = $("#pro_color").val();
    var pro_size = $("#pro_size").val();
    var pro_weight = $("#pro_weight").val();
    var pro_cm = $("#pro_cm").val();

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'sessionid': getCookie('sessionid'),
            'Content-Type': 'application/vnd.api+json',
        },
        url: '/api/inventory/product/',

        data: JSON.stringify({
            "data": {
                "type": "Product",
                "id": null,
                "attributes": {
                    "sku": sku,
                    "product_name": p_name,
                    "price": pro_pr,
                    "tax": pro_tax,
                    "product_description": pro_des,
                    "color": pro_color,
                    "size": pro_size,
                    "weight": pro_weight,
                    "image": "",
                    "comment": pro_cm,
                    "brand":  "/api/inventory/brand/"+brand_id+"/",
                    "category":  "/api/inventory/category/"+category_id+"/",


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