
$('.filerBtn').on('click', function(e) {
    e.preventDefault();

    alert("hi");
});

$.ajax({
    method: "GET",
    url: "http://127.0.0.1:5000/map/?ref=/nby/apa/5168155500.html"
})
    .done(function( msg ) {

//        $('.content p.row a').each(function( index ){
//            console.log($(this).attr('href'));
//        })



        console.log(msg);
        alert("done!!!");
    })
    .fail(function() {
        alert( "error" );
    });