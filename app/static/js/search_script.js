// 
//  Subsidietrekker.nl
// 
//  search_script.js
// 

$("form").change(function (event) {
    // $.get("", $(this).serializeArray());
    $.get("_form_streamer", $(this).serializeArray());
});