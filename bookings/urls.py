"""bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/<str:id>', views.dashboard, name="dashboard"),
    path('update_client/<str:id>', views.update_client, name="update-client"),
    path('booking_form/<str:session>', views.book_session, name="booking-form"),
    path('session_form/<str:id>', views.select_session, name="select-session"),
    path('select_booking_time/<str:session>', views.select_booking_time, name="select-booking-time"),
]
