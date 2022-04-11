from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.signup),
    path('login/',views.login_user),
    path('user_profile/',views.user_profile),
    path('user_logout/',views.user_logout),
]
