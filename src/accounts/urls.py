from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('rest_framework_social_oauth2.urls')),
    path('fabriquant', views.AdminFabriquant.as_view()),
    path('fabriquant/utilisateur', views.FabriquantView.as_view()),
    path('',views.UserView.as_view())

]