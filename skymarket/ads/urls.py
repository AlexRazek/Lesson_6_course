from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from skymarket.ads import views

router = routers.SimpleRouter()

urlpatterns = [

    path(' ', views.root),
    path('ad/', views.AdListView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdUploadImageView.as_view()),
    path('comment/', views.CommentListView.as_view()),
    path('comment/<int:pk>', views.CommentRetrieveView.as_view()),
    path('comment/create/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view()),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls