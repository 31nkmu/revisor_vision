from django.urls import path

from plate import views

urlpatterns = [
    path('generate/', views.GeneratePlateApiView.as_view()),
    path('get/', views.ListPlateApiView.as_view()),
    path('add/', views.AddPlateApiView.as_view()),
]
