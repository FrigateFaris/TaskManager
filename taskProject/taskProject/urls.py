"""
URL configuration for taskProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from taskApp.views import show_start_page, show_create_page, edit_task_show_page, delete_task, is_done

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_start_page, name='start'),
    path('create/', show_create_page, name='create'),
    path('<int:pk>/', edit_task_show_page, name='edit'),
    path('delete/<int:pk>/', delete_task, name='delete'),
    path('done/<int:pk>/', is_done, name='done')
]
