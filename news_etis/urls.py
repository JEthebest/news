from django.urls import path, include
from .views import index, index_view

app_name='news_etis'

urlpatterns = [
    path('etis/', index, name='main'),
    path('pass/', index_view, name='index'),
]
        