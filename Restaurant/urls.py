"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from meals import urls as meals_url
from reservation import urls as reserve_url
from blog import urls as blog_url
from aboutus import urls as aboutus_url
from contactus import urls as contactus_url
from menu import urls as menu_url
from home import urls as home_url
from user import urls as user_url

from Restaurant import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('meals/', include(meals_url), name = 'meals'),
    path('reservation/', include(reserve_url), name='reservation'),
    path('blog/', include(blog_url), name='blog'),
    path('aboutus/', include(aboutus_url), name='aboutus'),
    path('contactus/', include(contactus_url), name='contactus'),
    path('menu/', include(menu_url), name='menu'),
    path('user/', include(user_url), name='user'),
    path('', include(home_url), name='home'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


