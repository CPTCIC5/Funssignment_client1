from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('profile-update/',views.profile_update,name='profile-update')
]
