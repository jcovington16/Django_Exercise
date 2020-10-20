from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='blog_page'),
    path('blog/new/', views.PostCreateView.as_view(), name='blog_new'),
    path('blog/<int:pk>/edit', views.PostUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete', views.PostDeleteView.as_view(), name='blog_delete')
]
