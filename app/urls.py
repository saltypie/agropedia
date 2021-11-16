from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
urlpatterns=[
 path("api/ai/", views.PlantsSuggest.as_view(), name="apisuggest")   
]
 