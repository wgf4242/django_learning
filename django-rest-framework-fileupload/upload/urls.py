"""upload URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.mdself.views import CategoryViewSet
from upload import settings
from urltest.views import ImageViewSet

router = DefaultRouter()
router.register(r'imgs', ImageViewSet, base_name="img")
router.register(r'categories', CategoryViewSet, base_name="category")

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('file/', include('up1.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
