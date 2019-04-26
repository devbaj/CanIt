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
    $.ajax({
        method: "GET",
        url: "/sidebar"
    })
    .done(function(res) {
        $('#sidebar').html(res)
    })
    // ======================================================= //
    //                    DROPDOWN MENU                        //
    // ======================================================= //
    $('.header').on('click', '#menu-icon', function() {
        $('.header__menu ul').toggleClass('header__menulist--hidden header__menulist--visible');
    })

    $('html').click(function(e) {
        if ($(e.target).hasClass("header__menuicon")) {
        }
        else {
            if($('.header__menu ul').hasClass('header__menulist--visible')) {
                $('.header__menu ul').removeClass('header__menulist--visible');
                $('.header__menu ul').addClass('header__menulist--hidden');
            }
        }
    })
});