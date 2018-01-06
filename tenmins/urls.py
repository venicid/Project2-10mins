"""tenmins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from website.views import listing,detail_login, detail_register, detail,detail_voter_post
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^listing/$', listing, name='listing'),
    url(r'^listing/(?P<cate>[A-Za-z]+)$', listing, name='listing'),  # cate变量
    url(r'^login/$', detail_login, name='detail_login'),
    url(r'^register/$', detail_register, name='detail_register'),
    url(r'^logout/$', logout, {'next_page':'/listing'}, name='logout'),
    url(r'^detail/(?P<page_num>\d+)$', detail, name='detail'),
    url(r'^detail/vote/(?P<page_num>\d+)$', detail_voter_post, name='detail_voter_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

