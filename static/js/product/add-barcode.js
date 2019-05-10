 var sku = "inventro123";

        $("#product_barcode").click(function() {

            $("#barcode").JsBarcode(sku,{
                width: 2,
                height: 100,
                format: "code128",
                displayValue: true,
                fontOptions: "",
                font: "monospace",
                text: undefined,
                textAlign: "center",
                textPosition: "bottom",
                textMargin: 2,
                fontSize: 20,
                background: "#ffffff",
                lineColor: "#000000",
                margin: 10,
                marginTop: undefined,
                marginBottom: undefined,
                marginLeft: undefined,
                marginRight: undefined,
                valid: function valid() {}
            });

        });

            $('#save_barcode').click(function() {
        download($('#barcode').attr('src'),sku+".png","image/png");
        });