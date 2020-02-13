"""simplesocial URL Configuration

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
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    # path('userdetails/', views.userDetails),
    # path('display/', views.userDetails),
    path('admin/', admin.site.urls),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('posts/', include("posts.urls", namespace="posts")),
    path('groups/',include("groups.urls", namespace="groups")),
    path('MachineLearningApi/',include("MachineLearningApi.urls", namespace="MachineLearningApi")),
    path('MachineLearningApi/preprocess/', views.PreprocessPage.as_view(), name="preprocess"),
    
    path('MachineLearningApi/preprocess/partitiondata/',views.partitiondata.as_view(),name='partitiondata'),
    path('MachineLearningApi/preprocess/partitiondata/CreateModel/',views.CreateModel.as_view(),name='CreateModel'),
    
    
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)