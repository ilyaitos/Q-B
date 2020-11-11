



$ (document).ready(function (){

    $("#id12").click(function (e){
        $.post(
            "aj",
            {
                "a" : "helo"
            },
            function (resp) {
                alert(resp.mess)
            }
        );
    })





});







