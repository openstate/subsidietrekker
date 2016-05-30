// 
// Subsidietrekker.nl
// 
// datatables_script.js
// 

var entities = {
    overheid: true,
    ontvanger: true,
    regeling: true,
    Beleidsartikel: true

}

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

        "dom": 'Bfrtip',        
        "buttons": [
            {
                text: 'Overheid',
                action: function ( e, dt, node, config ) {
                    
                    if(entities.overheid) {
                        entities.overheid = false
                    } else {
                        entities.overheid = true
                    }
                    console.log("overheid: " + entities.overheid);
                }                
            },

            {
                text: 'Ontvanger',
                action: function (e, dt, node, config) {
                    if(ontvanger.overheid) {
                        ontvanger.overheid = false
                    } else { 
                        ontvanger.overheid = true
                    }
                    console.log("ontvanger: " + ontvanger.overheid);
                }
            },

            {
                text: 'Regeling',
                action: function (e, dt, node, config) {
                    if(regeling.overheid) {
                        regeling.overheid = false
                    } else { 
                        regeling.overheid = true
                    }
                    console.log("regeling: "+regeling.overheid);
                }
            },

            {
                text: 'Beleidsartikel',
                action: function (e, dt, node, config) {
                    if(beleidsartikel.overheid) {
                        beleidsartikel.overheid = false
                    } else { 
                        beleidsartikel.overheid = true
                    }
                    console.log("beleidsartikel: " +beleidsartikel.overheid);
                }
            },

        ],


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