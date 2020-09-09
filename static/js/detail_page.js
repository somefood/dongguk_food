$(document).ready(function () {
    getPage(1)
});

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

$(document).on('click', '[class*=update-comment]', function(e){
    var toolBox = e.target.parentElement
    var textBox = e.target.parentElement.previousElementSibling.previousElementSibling;
    var textOrigin = $(textBox).children().clone();
    var textComment = $(textBox).find('.text-comment')[0].innerHTML;
    var html = `
        <div class="CommentWriter">
            <div class="comment_inbox">
                <textarea class="comment_inbox_text">${textComment}</textarea>
            </div>
            <div class="comment_attach">
                <div class="register_box">
                    <a href="javascript:void(0)" class="btn btn-outline-primary btn_cancel">취소</a>
                    <a href="javascript:void(0)" class="btn btn-primary btn_register" onclick="registerComment(this)">등록<a>
                </div>
            </div>
        </div>`;
    $(textBox).empty().append(html);
    $(toolBox).css({"display": "none"});
    $(document).on('click', '[class*=btn_cancel]', function(){
       $(textBox).empty().append(textOrigin);
       $(toolBox).css({"display": "block"});
    });
});

function registerComment(obj){
    var result = confirm('등록하시겠습니까?');
    if (result) {
        var parent = $(obj).parents()[5];
        var text = $(obj).parents()[2].children[0].children[0];
        var textArea = $(text).val();
        $.ajax({
            type: "POST",
            url: `${MyGlobal.commentListUrl}update/${parent.id}/`,
            data: {text: textArea, csrfmiddlewaretoken: MyGlobal.csrfmiddlewaretoken},
            success: function (response) {
                if (response.is_updated) {
                    $(parent).empty().append(response.html);
                }
            }
        });
    }
}

function deleteComment(obj){
    var result = confirm('삭제하시겠습니까?')
    if (result) {
        var parent = obj.parentElement.parentElement.parentElement;
        $.ajax({
            type: "GET",
            url: `${MyGlobal.commentListUrl}delete/${parent.id}/`,
            success: function (response) {
                if (response.is_deleted) {
                    parent.remove();
                }
            }
        })
    }
}

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
});