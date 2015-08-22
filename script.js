
$('.filerBtn').on('click', function(e) {
    e.preventDefault();

    alert("hi");
});

$.ajax({
    method: "GET",
    url: "https://localhost:8000",
    data: { name: "John", location: "Boston" }
})
    .done(function( msg ) {
        console.log(msg);
        alert("done!!!");
    })
    .fail(function() {
        alert( "error" );
    });