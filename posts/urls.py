from django.urls import path
from .views import *

urlpatterns = [
    path('',PostListView.as_view() , name='posts-home'),
    path('about/', about, name='posts-about')
]