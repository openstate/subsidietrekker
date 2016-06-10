// 
// Subsidietrekker.nl
// 
// datatables_script.js
// 

var entities = {
    overheid: true,
    ontvanger: true,
    regeling: true,
    beleidsartikel: true
}

// var buttonCheck = function() {
//     entities = entities;
// }

$(function() {

    var table = $("#subs_list")
    .DataTable({

        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "http://localhost:5000/_streamer",
            "type": "GET",
            "data": {
                "buttons": entities,
            }
        },
        // "initComplete": function(settings, json) {
        //     buttonCheck();
        //   },

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
                    // table.ajax.reload(buttonCheck());
                }
            },

            {
                text: 'Ontvanger',
                action: function (e, dt, node, config) {
                    if(entities.ontvanger) {
                        entities.ontvanger = false
                    } else { 
                        entities.ontvanger = true
                    }
                    console.log("ontvanger: " + entities.ontvanger);
                }
            },

            {
                text: 'Regeling',
                action: function (e, dt, node, config) {
                    if(entities.regeling) {
                        entities.regeling = false
                    } else { 
                        entities.regeling = true
                    }
                    console.log("regeling: "+entities.regeling);
                }
            },

            {
                text: 'Beleidsartikel',
                action: function (e, dt, node, config) {
                    if(entities.beleidsartikel) {
                        entities.beleidsartikel = false
                    } else { 
                        entities.beleidsartikel = true
                    }
                    console.log("beleidsartikel: " +entities.beleidsartikel);
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