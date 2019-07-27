from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', BlogListView.as_view(), name= 'all-blogs'),
    path('blogger/<int:pk>/', BloggerBlogList.as_view(), name='blogger-details' ),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', BloggersListView.as_view(), name='all-bloggers'),
    path('blog/<int:pk>/newcomment/', BlogCommentCreate.as_view(), name='blog-newcomment')


]
