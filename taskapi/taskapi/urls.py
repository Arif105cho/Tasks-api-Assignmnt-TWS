"""
URL configuration for taskapi project.

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
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import TaskViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
    #generate api token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # add /remove /update memeber urls
    path('task/<int:pk>/add_member/', TaskViewSet.as_view({'post': 'add_member'}), name='task-add-member'),
    path('task/<int:pk>/remove_member/', TaskViewSet.as_view({'post': 'remove_member'}), name='task-remove-member'),
    path('task/<int:pk>/update_status/', TaskViewSet.as_view({'post': 'update_status'}), name='task-update-status'),
]
