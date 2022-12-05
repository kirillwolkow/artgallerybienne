from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('art-create/', views.ArtCreate.as_view(), name='art-create'),
    path('art-list/', views.ArtListView.as_view(), name='art-list'),
    path('art/<int:pk>', views.ArtDetailView.as_view(), name='art'),
]
