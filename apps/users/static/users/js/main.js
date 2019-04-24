$(document).ready(function(){
    alert("doc ready");
    $.ajax({
        method: "GET",
        url: "/header"
    })
    .done(function(res) {
        $('#header').html(res)
    })
})

function hideProfileMenu(){
    let dropDownMenu = $('.header__dropdown');
    let optionsMenu = $('.header__dropcontent');
    if(dropDownMenu.css('display') != "none") {
        dropDownMenu.css("display", "none");
    }
}