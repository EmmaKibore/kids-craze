from django.conf.urls import url, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)