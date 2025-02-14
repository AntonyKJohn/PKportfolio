from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView, DeletePostView, AddCategoryView, CategoryView


app_name = 'blog'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/',CategoryView, name='category'),
]