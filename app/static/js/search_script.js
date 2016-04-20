// 
//  Subsidietrekker.nl
// 
//  search_script.js
// 


// $("form").change(function (event) {
//     console.log($(this).serializeArray());
//     event.preventDefault;
// });

$("form").change(function (event) {
    $.get("", $(this).serializeArray());
    // $.post("", $(this).serializeArray());
});