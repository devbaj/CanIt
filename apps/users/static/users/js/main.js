$(document).ready(function() {
    console.log("doc ready");
    // ======================================================== //
    //                  LOAD PAGE COMPONENTS                    //
    // ======================================================== //
    $.ajax({
        method: "GET",
        url: "/header"
    })
    .done(function(res) {
        $('#header').html(res)
        console.log("header injected")
    });
    // ======================================================= //
    //                    DROPDOWN MENU                        //
    // ======================================================= //
    $('.header').on('click', '#menu-icon', function() {
        console.log("Dropdown button clicked")
        $('.header__menu ul').toggleClass('header__menulist--hidden header__menulist--visible');
    })
});