$(document).ready(function() {
    // ======================================================== //
    //                  LOAD PAGE COMPONENTS                    //
    // ======================================================== //
    $.ajax({
        method: "GET",
        url: "/header"
    })
    .done(function(res) {
        $('#header').html(res)
    });
    $.ajax({
        method: "GET",
        url: "/footer"
    })
    .done(function(res) {
        $('#footer').html(res)
    })
    // ======================================================= //
    //                    DROPDOWN MENU                        //
    // ======================================================= //
    $('.header').on('click', '#menu-icon', function() {
        console.log("Dropdown button clicked")
        $('.header__menu ul').toggleClass('header__menulist--hidden header__menulist--visible');
    })
});