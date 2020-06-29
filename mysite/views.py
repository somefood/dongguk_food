from django.contrib.auth.mixins import AccessMixin

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "게시글 작성자가 아닙니다."

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.writer:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AdminOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "관리자 권한이 아닙니다."

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)