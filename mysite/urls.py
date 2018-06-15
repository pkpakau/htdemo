from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/',core_views.admin,name="admin"),
  #url(r'^add_profile/(?P<id>)\d+',core_views.addprofile,name='add_profile'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)