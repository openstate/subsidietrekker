// 
//  Subsidietrekker.nl
// 
//  search_script.js
// 

$(document).ready(function(){
    $(#SearchForm).change(function (event) {
        console.log($(this).serializeArray());
        event.preventDefault;
    });
});