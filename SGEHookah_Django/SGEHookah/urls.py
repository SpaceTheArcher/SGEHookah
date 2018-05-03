"""SGEHookah URL Configuration

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
from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
  path('admindjango/', admin.site.urls),
	path('admin/', login, {"template_name":"index.html"}, name="login"),
	path('logout/', logout, {'next_page':'login'}, name="logout"),
	path('admin/home/', home, name="home"),
	path('', redirect_home),
	path('iframe/home/', iframe_home, name="iframe_home"),
	path('iframe/produtos/cadastrar/', cadastrar_produto, name="cadastrar_produto"),
	path('admin/usuario/', user_main, name="user_main"),
	path('iframe/vendas/calcula_frete', calcula_frete, name="calcula_frete")
]