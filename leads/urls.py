from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view() ),
    path('api/covid1/',views.covid1View.as_view() ),
    path('api/technews/',views.technewsView.as_view() ),
    path('api/worldnews/',views.worldnewsView.as_view() ),
    path('api/sportsnews/',views.sportsnewsView.as_view() ),
    path('api/weathernews/',views.weathernewsView.as_view() ),
    path('api/fullmore/',views.fullmoreView.as_view() ),
    path('api/posts/', views.PostView.as_view(), name= 'posts_list'),
]