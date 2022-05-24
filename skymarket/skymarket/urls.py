from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("admin/", admin.site.urls),
    path("redoc-tasks/", include("redoc.urls")),
    path("", include("users.urls")),
    path('ad/', include('ads.urls')),
    path('ad/<int:pk>', include('ads.urls')),
    path('ad/<int:pk>/update/', include('ads.urls')),
    path('ad/<int:pk>/delete/', include('ads.urls')),
    path('ad/<int:pk>/upload_image/', include('ads.urls')),
    path('comment/', include('ads.urls')),
    path('comment/<int:pk>', include('ads.urls')),
    path('comment/create/', include('ads.urls')),
    path('comment/<int:pk>/update/', include('ads.urls')),
    path('comment/<int:pk>/delete/', include('ads.urls')),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)