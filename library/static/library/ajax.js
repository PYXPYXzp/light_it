$(document).ready(function() {
    var btn = $(".books_author");
    btn.click(function () {
        var csrftoken = getCookie('csrftoken');
        var author_id = $(this).data("authorid");
        $.ajax({
            url: '/author_books/',
            type: 'get',
            data: {
                select_author: author_id
            },
            success: function (data) {
                $("#content").html(data);
            }
        })
    });
    $(".books_author[data-authorid="+author_id+"]").click();
});
