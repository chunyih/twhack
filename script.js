
$('.filerBtn').on('click', function(e) {
    e.preventDefault();

    $('.content p.row .txt .pl a').each(function(index){
        var $ele = $(this);

        var urlStr = $(this).attr('href');
        var maxTime = $('input#maxTime').val();
        console.log(maxTime);

        $.ajax({
            method: "GET",
            url: "http://127.0.0.1:5000/map/?ref=" + urlStr + "&maxTime=" + maxTime
        })
            .done(function(msg) {
                console.log(urlStr + ": " + msg);
                if (msg!=='True'){
                    $ele.parents('p').hide();
                }

            })
            .fail(function() {
                $ele.parents('p').hide();
                console.log("ERROR..");
            })
    });

});




//var urlStr = $('.content p.row .txt .pl a').attr('href');
//
//
//$.ajax({
//    method: "GET",
//    url: "http://127.0.0.1:5000/map/?ref=" + urlStr
//})
//    .done(function(msg) {
//        console.log(urlStr + ": " + msg);
//    })
//    .fail(function() {
//        alert( "error" );
//    });