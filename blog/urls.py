from django.urls import path
from blog import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='blog/',permanent=True)),
    path('blog/', views.index,name='index'),
    path('blog/blogs', views.PostListView.as_view(),name='posts'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('blog/bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/blogger/<int:pk>', views.BloggerDetailView.as_view(),name='blogger-detail'),
    path('blog/<int:pk>/create', views.CommentCreateView.as_view(), name='create_comment'),
]
