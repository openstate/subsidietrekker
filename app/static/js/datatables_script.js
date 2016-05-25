// 
// Subsidietrekker.nl
// 
// datatables_script.js
// 

$(function() {

    var table = $("#subs_list")
    .DataTable({

        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "http://localhost:5000/_streamer",
            "type": "GET",
            "data": {
                "test": "zisiztezt",
                "tast": 12342542
            }
        },


        "columns": [
            { "data": "overheid", "name": "overheid" },
            { "data": "regeling", "name": "regeling" },
            { "data": "ontvanger", "name": "ontvanger" },
            { "data": "beleid", "name": "beleid" },
            { "data": "realisatie", "name": "realisatie" },
            { "data": "jaar", "name": "jaar" }
        ],



    });

    table.on( 'order.dt',  function () { console.log( 'Order' ); } )
    .on( 'search.dt', function () {
        console.log( 'Search for '+table.search() );

        d3.json('http://localhost:5000/_viz_streamer?query='+table.search(), function(error, json) {
            if (error) return console.warn(error);
            data = json;

            // Update the SVG with the new data and call chart
            chart_data.datum(data).transition().duration(500).call(chart);
            nv.utils.windowResize(chart.update);
        });
    } )
    .on( 'page.dt',   function () { console.log( 'Page' ); } )

})