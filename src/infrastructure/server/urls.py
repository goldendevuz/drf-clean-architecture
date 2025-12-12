"""forex URL Configuration

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

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from debug_toolbar.toolbar import debug_toolbar_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from src.infrastructure.settings.config import ADMIN_URL, REDOC_URL, SWAGGER_URL


urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path('api/', include((f'{settings.API_ROUTES}.urls', 'api'), namespace='api')),
    
    path('api-auth/', include('rest_framework.urls')),  # Important for login/logout
    path('schema-viewer/', include('schema_viewer.urls')),
    
    # Spectacular schema and UI docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(SWAGGER_URL, SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(REDOC_URL, SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + debug_toolbar_urls()
