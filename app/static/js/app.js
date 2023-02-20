/* Add your Application JavaScript */

$(document).ready(function(){

    $(".invalid").on('click',function(){
        $(this).removeClass("invalid");
    });

    (function(){
        setTimeout(function(){$('.alert').fadeOut("fast");}, 8000);
    })();

});