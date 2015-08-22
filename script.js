
$('.filerBtn').on('click', function(e) {
    e.preventDefault();

    alert("hi");
});

$('.content p.row a').each(function(index){
    var urlStr = $(this).attr('href');
    console.log(urlStr);

//    $.ajax({
//        method: "GET",
//        url: "http://127.0.0.1:5000/map/?ref=" + urlStr
//    })
//    .done(function(msg) {
//        console.log(urlStr + ": " + msg);
//    })
//    .fail(function() {
//        alert( "error" );
//    })
});

//
//var urlStr = $('.content p.row a').attr('href');
//
//$.ajax({
//    method: "GET",
//    url: "http://127.0.0.1:5000/map/?ref=" + urlStr
//})
//    .done(function(msg) {
//        console.log(msg);
//        alert("done!!!");
//    })
//    .fail(function() {
//        alert( "error" );
//    });