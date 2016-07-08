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

        "dom": 'Bfrtip',        
        "buttons": [
            {
                text: 'Overheid',
                action: function ( e, dt, node, config ) {
                    entities.overheid = !entities.overheid;
                    console.log("overheid: " + entities.overheid);
                    if (entities.overheid) {
                        $('a.dt-button:eq(0)').css('background-color', 'yellow');
                    } else {
                        $('a.dt-button:eq(0)').css('background-color', 'purple');
                    }
                }
            },

            {
                text: 'Ontvanger',
                action: function (e, dt, node, config) {
                    entities.ontvanger = !entities.ontvanger;
                    console.log("ontvanger: " + entities.ontvanger);
                    if (entities.ontvanger) {
                        $('a.dt-button:eq(1)').css('background-color', 'yellow');
                    } else {
                        $('a.dt-button:eq(1)').css('background-color', 'purple');
                    }
                }
            },

            {
                text: 'Regeling',
                action: function (e, dt, node, config) {
                    entities.regeling = !entities.regeling;
                    console.log("regeling: "+entities.regeling);
                    if (entities.regeling) {
                        $('a.dt-button:eq(2)').css('background-color', 'yellow');
                    } else {
                        $('a.dt-button:eq(2)').css('background-color', 'purple');
                    }
                }
            },

            {
                text: 'Beleidsartikel',
                action: function (e, dt, node, config) {
                    entities.beleidsartikel = !entities.beleidsartikel;
                    console.log("beleidsartikel: " + entities.beleidsartikel);
                    if (entities.beleidsartikel) {
                        $('a.dt-button:eq(3)').css('background-color', 'yellow');
                    } else {
                        $('a.dt-button:eq(3)').css('background-color', 'purple');
                    }
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
    .on( 'search.dt', function (e, settings) {
        settings.ajax.data.buttons = entities;
        console.log( 'Search for '+table.search() );

        var field_names = Object.keys(entities);
        var fields_for_request = field_names.map(function (f) {return 'buttons[' + f + ']=' + (entities[f] ? 'true' : 'false')});
        d3.json('http://localhost:5000/_viz_streamer?query='+table.search() + '&' + fields_for_request.join('&'), function(error, json) {
            if (error) return console.warn(error);
            data = json;

            // Update the SVG with the new data and call chart
            chart_data.datum(data).transition().duration(500).call(chart);
            nv.utils.windowResize(chart.update);
        });
    } )
    .on( 'page.dt',   function () { console.log( 'Page' ); } )

})