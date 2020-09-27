"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include,url
from django.contrib import admin
from share.views import HomeView,DisplayView,MyView,SearchView,delFile,AllView
from django.urls import path


urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(), name="home"),
    url(r'^s/(?P<code>\d+)/$',DisplayView.as_view()),#即匹配127.0.0.1:9000/s/15156.../这样的请求,?P<code>只是给那个组命名
    url(r'^my/$',MyView.as_view(),name="MY"),
    url(r'^all/$',AllView.as_view(),name="All"),
    url(r'^search/',SearchView.as_view(),name="search"),
    path('delFile',delFile,name='delFile'),
   # path('testApi',testApi,name='testApi'),
]
