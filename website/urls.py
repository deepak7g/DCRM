from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('logoutUser/', views.logoutUser, name='logout' ),
    path('registerUser/', views.registerUser, name='register' ),
    path('record/<int:pk>', views.customerRecord, name='record' ),
    path('deleteRecord/<int:pk>', views.deleteRecord, name='deleteRecord' ),
    path('addRecord/', views.addRecord, name='addRecord' ),
    path('UpdateRecord/<int:pk>', views.UpdateRecord, name='UpdateRecord' ),

    ]
