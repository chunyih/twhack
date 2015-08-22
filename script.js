
$('.filerBtn').on('click', function(e) {
    e.preventDefault();

    alert("hi");
});

$.ajax({
    method: "GET",
    url: "http://localhost:5000/map/?ref=/nby/apa/5168155500.html"
})
    .done(function( msg ) {
        console.log(msg);
        alert("done!!!");
    })
    .fail(function() {
        alert( "error" );
    });