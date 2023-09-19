"""TheControlHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from NanoWareControl.views import camera2, camera3, home, livecameras, monitor, logs, camera1, camera2, camera3, camera4, log #, image_camera1_page, image_camera2_page, image_camera3_page, image_camera4_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('livecameras/', livecameras, name='livecameras'),
    path('livecameras/camera1', camera1, name='camera1'),
    path('livecameras/camera2', camera2, name='camera2'),
    path('livecameras/camera3', camera3, name='camera3'),
    path('livecameras/camera4', camera4, name='camera4'),
    path('monitor/', monitor, name='monitor'),
    path('logs/', logs, name='logs'),
    path('log/<int:logid>', log, name='log'),
]
