"""softwareCup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from pageFrame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('register/res/', views.reg_result),
    path('index/', views.index),
    path('index2/', views.index2),

    path('show/avg/data/', views.show_avg_data),
    path('show/four/classes/data/', views.show_four_classes),
    path('show/pre/data/', views.show_pre_data),

    path('show/pre/top5/', views.show_pre_top5),

    path('show/avg/echarts/', views.show_avg_echarts),
    path('show/three/types/', views.show_three_class),

    path('show/pre/user/type/', views.show_pre_user_type5),

    path('show/cla/echarts/data/', views.get_cla_echarts_data),

    path('show/two/line/data/', views.get_two_line_echarts),

    path('show/two/sketches/', views.get_two_sketches),
    path('exit/', views.exit)
]
