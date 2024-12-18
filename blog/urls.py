from django.urls import path

from blog.views import homepage

urlpatterns = [
    path('', homepage)
]