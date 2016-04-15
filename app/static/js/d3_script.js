// 
// Subsidietrekker.nl
// 
//  d3_script.js
// 

var data;

d3.json('http://localhost:5000/_streamer', function(error, json) {
    if (error) return console.warn(error);
    data = json;

    height = 960;
    width = 540;

    nv.addGraph(function() {
        var chart = nv.models.pieChart()
            .x(function(d) {return d.key})
            .y(function(d) {return d.doc_count})
            .showLabels(true);

        d3.select("#chart svg")
            .datum(data)
            .transition().duration(350)
            .call(chart);

        nv.utils.windowResize(chart.update);
        return chart;
    });
});