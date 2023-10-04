

from django.urls import path
from . import views

urlpatterns = [
    path('links/', views.LinkListCreateView.as_view(), name='link-list-create'),
    path('<str:shorten_prefix>/', views.redirect_to_original_url, name='redirect-to-original-url'),
]
