from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us_view, name='about-us'),
    path('art-create/', views.ArtCreate.as_view(), name='art-create'),
    path('art-list/', views.ArtListView.as_view(), name='art-list'),
    path('art/<int:pk>/', views.ArtDetailView.as_view(), name='art-detail'),
    path('profile/<int:pk>/', views.user_profile, name='profile'),
    path('like/<int:pk>/', views.like_view, name='like-post'),
]
