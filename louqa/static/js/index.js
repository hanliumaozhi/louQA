$(document).ready(function() {
    $("#nav-index").addClass("current_page_item");
    $("#submit-button").click(function(){
        var name = $("#name").val();
        var email = $("#email").val();
        var password = $("#password").val();
        var post_url = $("#signup-data").attr("url");
        $.post(post_url, {"name": name, "email": email, "password": password}, function(data){
            if(data.status=="success"){
                $(".panel-pop h2 i").trigger("click");
            }
            alert(data.info);
        });
    });
});
