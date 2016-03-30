$(function() {

    $("#subs_list").DataTable({

        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "http://localhost:5000/_ajax_streamer"
        },


        "columns": [
            { "data": "overheid", "name": "overheid" },
            { "data": "regeling", "name": "regeling" },
            { "data": "ontvanger", "name": "ontvanger" },
            { "data": "beleid", "name": "beleid" },
            { "data": "realisatie", "name": "realisatie" },
            { "data": "jaar", "name": "jaar" }
        ]

    });
})