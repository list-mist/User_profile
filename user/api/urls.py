from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.api_detail),
    path('api_update/',views.api_update),

]
