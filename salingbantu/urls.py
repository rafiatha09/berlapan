from django.urls import path

from . import views

app_name = 'salingbantu'

urlpatterns = [
    path('', views.SalingBantu.as_view(), name='salingbantu'),
    path('details/<int:pk>', views.DetailsPost.as_view(), name='details_post'),
    path('details/<int:pk>/comment', views.AddComment.as_view(), name='add_comment'),
    path('add-post/', views.AddPost.as_view(), name='add_post'),
]