from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
     path('<int:id>/', views.show, name='movies.show'),
    path('petitions/', views.petitions_list, name='movies.petitions'),
    path('petitions/create/', views.petition_create, name='movies.petition_create'),
    path('petitions/<int:id>/vote/', views.petition_vote, name='movies.petition_vote'),
]