"""
URL configuration for cloudpy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from home import views as home_view
from accounts import views as accounts_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.index, name='home'),
    path('signup/', accounts_view.signup_view, name='signup'),
    path('login/', accounts_view.login_view, name='login'),
    path('logout/', accounts_view.logout_view, name='logout'),
    path('manim/',include('manim.urls')),
    path('donate/', home_view.donate, name='donate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
