from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact),
    path('snippet', views.snippet_detail),

]
