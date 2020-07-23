"""ClubProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from club import views
from club.views import IndexView,ThanksView,ReservationView,ReservationCompleteView,ReservationTimeView,ReservationCancelView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name = 'index'),
    path('thanks',ThanksView.as_view(),name = 'thanks'),
    path('reservation',ReservationView.as_view(),name = 'reservation'),
    path('reservation/<int:pk>/', views.ReservationTimeView.as_view(), name='Reservation-times'),
    path('reservation_complete',ReservationCompleteView.as_view(),name = 'Reservation-complete'),
    path('reservation/cancel',ReservationCancelView.as_view(),name = 'Reservation-cancel'),

]
