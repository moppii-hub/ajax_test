from django.contrib import admin
from django.urls import path
from . import views
app_name = "app"

urlpatterns = [
    path('', views.post_list, name="ajax_post_list"),
    path('ajax/', views.ajax_post_add, name="ajax_post_add"),
    path('ct/', views.clicktest_list, name="clicktest_list"),
    path('ct_add/', views.clicktest_add, name="clicktest_add"),
]

