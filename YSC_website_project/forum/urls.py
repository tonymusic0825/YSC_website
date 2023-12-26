from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='forum'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>', views.show_post, name='show_post'),
    path('post/<int:pk>/edit_post', views.edit_post, name='edit_post')
]