"""MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import (index, JuegoList, JuegoDetail, 
                        JuegoCreate, JuegoUpdate, JuegoDelete, 
                        SignUp, Login, Logout, ProfileUpdate)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='base'),
    path('juego/list', JuegoList.as_view(), name='juego-list'),
    path('juego/<pk>/detail', JuegoDetail.as_view(), name='juego-detail'),
    path('juego/create', JuegoCreate.as_view(), name='juego-create'),
    path('juego/<pk>/update', JuegoUpdate.as_view(), name='juego-update'),
    path('juego/<pk>/delete', JuegoDelete.as_view(), name='juego-delete'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'), #Link principal / Esta ruta de logeo, la concidero la primera vista a ver, tenemos el index claramente, pero al sacarla me salta muchos errores.
    path('logout/', Logout.as_view(), name='logout'), 
    path('profile/<pk>/update', ProfileUpdate.as_view(), name='profile-update'), 
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)