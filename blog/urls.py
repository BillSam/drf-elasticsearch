from django.urls import path, include
from rest_framework import routers

from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet
