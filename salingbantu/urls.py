from django.urls import path

from . import views

app_name = 'salingbantu'

urlpatterns = [
    path('salingbantu/', views.SalingBantu.as_view(), name='salingbantu'),
    path('salingbantu/details/<int:pk>', views.DetailsPost.as_view(), name='details_post'),
    path('salingbantu/details/<int:pk>/comment', views.AddComment.as_view(), name='add_comment'),
    path('salingbantu/add-post/', views.AddPost.as_view(), name='add_post'),
]