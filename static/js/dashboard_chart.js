    //Depleting Products
    var ctx = document.getElementById("product-sell").getContext('2d');
    var value = [10, 125, 25, 200]; // Fring added-dummy data
    var Productlabel = ['yoyo', 'Car', 'Gun', 'Doll']; //Fring added- dummy product name
    var productColors = [];
    //loop for color selection for varies stage of product amount
    for (var i = 0; i < value.length; i++) {
        if (value[i] <= 10) {
            productColors[i] = "#e16262";
        } else if (value[i] <= 20) {
            productColors[i] = "#fabc60";
        } else if (value[i] <= 30) {
            productColors[i] = "#ff9db2";
        } else {
            productColors[i] = "#81cdff";
        }

    }
    //Depleting Product chart properties starts here
    var myProductChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Productlabel,
            datasets: [{
                label: 'Products',
                data: value,
                backgroundColor: productColors,
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            legend: {
                display: false, // for not displaying the label
                position: 'right',
                labels: {
                    fontColor: '#000000'
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },

        }
    });
    //end of Depleting product chart

    //Star Products
    var totalSellChart = document.getElementById("total-sell").getContext('2d');
    var monthLabels = ["yoyo", "toyGun", "doll", "toyHouse", "car", "waterGun"]; //Fring added- dummy data
    var totalSell = [500, 600, 750, 550, 345, 800];//Fring added- dummy data
    var totalSellColors = []; //unused color array

    //Star productsS chart properties starts here
    var mySellChart = new Chart(totalSellChart, {
        type: 'bar',
        data: {
            labels: monthLabels,
            datasets: [{
                label: '', //empty label
                data: totalSell,
                backgroundColor:
                    'rgba(54, 162, 235, 0.2)',
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            legend: {
                display: false, // for not displaying the label
                position: 'right'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },

        }
    });
    //end of Total Sell chart

    //Dog Products
    var StockChart = document.getElementById("stock").getContext('2d');
    var stockValue = [90, 700, 250, 440, 190, 800];//fring added- dummy data
    var stockProduct = ["yoyo", "toyGun", "doll", "toyHouse", "car", "waterGun"];//fring added- dummy data
    var stockColor = [];

    //loop for color selection for varies stage of product amount in stock
    // for (var i = 0; i < stockValue.length; i++) {
    //     if (stockValue[i] <= 100) {
    //         stockColor[i] = "red";
    //     } else if (stockValue[i] <= 200) {
    //         stockColor[i] = "yellow";
    //     } else if (stockValue[i] <= 300) {
    //         stockColor[i] = "blue";
    //     } else {
    //         stockColor[i] = "green";
    //     }
    //
    // }
    //Dog Products properties starts here
    var myStockChart = new Chart(StockChart, {
        type: 'bar',
        data: {
            labels: stockProduct,
            datasets: [{
                label: '', //empty label
                data: stockValue,
                backgroundColor:'rgba(54, 162, 235, 0.2)',
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            legend: {
                display: false, // for not displaying the label
                position: 'right',
                labels: {
                    fontColor: '#000000'
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
    //Stock chart properties ends here


