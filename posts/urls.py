from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('contact', views.contact_us, name='contact'),
    path('about', views.about, name='about'),
    path('', views.post_list, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('search/', views.search, name='search'),
]
