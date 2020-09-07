function getPage(n) {
    $.ajax({
        type: "GET",
        url: MyGlobal.commentListUrl,
        data: {
            page: n
        },
        success: function (response) {
            $('.comment-wrapper').empty().append(response);
        },
        error: function (error) {
            console.log(error)
        }
    })
}

$(document).ready(function () {
    getPage(1)
});

$('#multiForm').on('submit', function (e) {
    e.preventDefault();
    var formData = $(this).serialize();

    $.ajax({
        type: "POST",
        url: MyGlobal.commentCreateUrl,
        cache: false,
        data: formData,
        success: function (response) {
            if (!response.authenticated) {
                alert('로그인 해주세요.')
                window.location.href = `/accounts/login?next=${MyGlobal.detailUrl}`;
            } else {
                $('#multiForm')[0].reset();
                getPage(response.last_page);
            }
        },
        error: function (response) {
            alert('bye');
        }
    })
})