from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('contact', views.contact_us, name='contact'),
    path('about', views.about, name='about'),
    path('', views.post_list, name='index'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('search/', views.search, name='search'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
