$(document).ready(function () {
    $('.carousel-item:first-child').addClass('active');
});

$("[class*=like]").click(function () {
    var pk = $(this).attr('post-id');
    $.ajax({
        type: "GET",
        url: MyGlobal.url,
        data: {'pk': pk},
        dataType: "json",
        success: function (response) {
            $("#count-" + pk).html(response.like_count + "개");
            var users = $("#like-user-" + pk).text();
            if (response.message) {
                $('#like-heart-'+pk).removeClass('far fa-heart').addClass('fas fa-heart');
            } else {
                $('#like-heart-'+pk).removeClass('fas fa-heart').addClass('far fa-heart');
            }
        },
        error: function (request, status, error) {
            alert("로그인이 필요합니다!")
            window.location.replace("/accounts/login/")
        }
    })
});