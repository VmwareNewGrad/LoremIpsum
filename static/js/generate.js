function getLorem() {

var area = document.getElementById("textOutput");
var n = document.getElementById("123").value;

if(document.getElementById('paraPick').checked) {

   $.ajax({
            url: '/getP?num='+n,
            success: function(response) {
                area.innerHTML = response;
            },
            error: function(error) {
                alert(error);
            }
        });

} else if(document.getElementById('wordPick').checked) {

    $.ajax({
            url: '/getW?num='+n,
            success: function(response) {
                area.innerHTML = response;
            },
            error: function(error) {
                alert(error);
            }
        });


} else if(document.getElementById('letterPick').checked) {

    $.ajax({
            url: '/getL?num='+n,
            success: function(response) {
                area.innerHTML = response;
            },
            error: function(error) {
                alert(error);
            }
        });


} else {
    alert("error: No radio button checked");
}
}
