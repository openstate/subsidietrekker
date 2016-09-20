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
        "language": {
          "url": "//cdn.datatables.net/plug-ins/1.10.12/i18n/Dutch.json"
        },
        "responsive": true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/_streamer",
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
                     $('a.dt-button:eq(0)').removeClass('button-unclicked');
                    } else {
                     $('a.dt-button:eq(0)').addClass('button-unclicked');
                    }
                    $("#subs_list").DataTable().ajax.reload();
                }
            },

            {
                text: 'Ontvanger',
                action: function (e, dt, node, config) {
                    entities.ontvanger = !entities.ontvanger;
                    console.log("ontvanger: " + entities.ontvanger);
                    if (entities.ontvanger) {
                        $('a.dt-button:eq(1)').removeClass('button-unclicked');
                    } else {
                        $('a.dt-button:eq(1)').addClass('button-unclicked');
                    }
                    $("#subs_list").DataTable().ajax.reload();
                }
            },

            {
                text: 'Regeling',
                action: function (e, dt, node, config) {
                    entities.regeling = !entities.regeling;
                    console.log("regeling: "+entities.regeling);
                    if (entities.regeling) {
                        $('a.dt-button:eq(2)').removeClass('button-unclicked');
                    } else {
                        $('a.dt-button:eq(2)').addClass('button-unclicked');
                    }
                    $("#subs_list").DataTable().ajax.reload();
                }
            },

            {
                text: 'Beleidsartikel',
                action: function (e, dt, node, config) {
                    entities.beleidsartikel = !entities.beleidsartikel;
                    console.log("beleidsartikel: " + entities.beleidsartikel);
                    if (entities.beleidsartikel) {
                        $('a.dt-button:eq(3)').removeClass('button-unclicked');
                    } else {
                        $('a.dt-button:eq(3)').addClass('button-unclicked');
                    }
                    $("#subs_list").DataTable().ajax.reload();
                }
            },

        ],


        "columns": [
            { "data": "overheid", "name": "overheid" },
            { "data": "ontvanger", "name": "ontvanger" },
            {
              "data": "realisatie",
              "name": "realisatie",
              "className": "dt-right",
              render: function ( data, type, row ) {
                return accounting.formatMoney(data, "€", 2, ".", ",");
              }
            },
            { "data": "jaar", "name": "jaar" },
            { "data": "regeling", "name": "regeling" },
            { "data": "beleid", "name": "beleid" }
        ],


    });

    table.on( 'order.dt',  function () { console.log( 'Order' ); } )
    .on( 'init.dt', function () {
      $('.dt-buttons').prepend($('<div style="display: inline-block;margin-right: 15px;">Zoeken op:</div>'));
    })
    .on( 'search.dt', function (e, settings) {
        settings.ajax.data.buttons = entities;
        console.log( 'Search for '+table.search() );

        var field_names = Object.keys(entities);
        var fields_for_request = field_names.map(function (f) {return 'buttons[' + f + ']=' + (entities[f] ? 'true' : 'false')});
        d3.json('/_viz_streamer?query='+table.search() + '&' + fields_for_request.join('&'), function(error, json) {
            if (error) return console.warn(error);
            data = json;

            // Update the SVG with the new data and call chart
            chart_data.datum(data).transition().duration(500).call(chart);
            nv.utils.windowResize(chart.update);
        });
    } )
    .on( 'page.dt',   function () { console.log( 'Page' ); } )

})
