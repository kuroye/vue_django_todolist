"""
URL configuration for todolist project.

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
from django.urls import path, include
from rest_framework_simplejwt import views as simplejwt_views  # 引入simplejwt

from user.views import CustomTokenObtainPairView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/todo', include('todo.urls')),
    path('api/ability', include('ability.urls')),
    path('api/user', include('user.urls')),

    path('api-auth/', include('rest_framework.urls')),  # drf 认证url
    # path('api-token-auth/', views.obtain_auth_token),  # drf token获取的url
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # simplejwt认证接口
    path('api/token/refresh/', simplejwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # simplejwt认证接口
    # path('ckeditor/', include('ckeditor_uploader.urls')),  # 配置富文本编辑器url

]