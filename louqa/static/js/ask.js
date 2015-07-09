$(document).ready(function() {
    $("#nav-ask").addClass("current_page_item");
    $("#publish-question").click(function(){
        var title = $("#question-title").val();
        var content = $("#question-details").val();
        var post_url = $("#question-data").attr("url");
        $.post(post_url, {"title": title, "content": content }, function(data){
            alert(data.info);
        });
    });
});
