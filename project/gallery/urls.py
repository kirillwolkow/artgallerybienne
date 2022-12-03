from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('art-create/', views.ArtCreate.as_view(), name='art-create'),
]
