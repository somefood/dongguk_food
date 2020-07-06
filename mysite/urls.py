from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from store.models import Store
from board.models import UserBoard

class HomePageView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store_list'] = Store.objects.filter(category='restaurant')[:1] | \
                                Store.objects.filter(category='bar')[:1] | \
                                Store.objects.filter(category='cafe')[:1]

        return context

urlpatterns = [
    path('board/', include('board.urls')),
    path('store/', include('store.urls')),
    path('helpers/', include('helpers.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
#   path('accounts/', include('django.contrib.auth.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]

if settings.DEBUG:
    if settings.DEBUG:
        import debug_toolbar
        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

