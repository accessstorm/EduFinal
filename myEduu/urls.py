#own

from django.urls import path
from . import views
from .views import PostView, ShowView, AddPost, UpdatePost, DeletePost, AddCategoryView, CategoryView, LikeView, AddCommentView



urlpatterns = [
    path('', views.home, name='home'),
    path('login.html', views.login, name='login'),
    path('error.html', views.error, name='error'),
    path('loginT.html', views.loginT, name='loginTeacher'),
    #path('',HomeView.as_view(), name = 'home'),
    path('all_categories.html', views.Cato, name='all_categories'),
    path('category/<str:cats>/', views.CategoryView, name = 'category'),
    
    #class based urls
    path('view1.html', PostView.as_view(), name="view1"),
    path('post/<int:pk>', ShowView.as_view(), name="view2"),
    path('postT/', AddPost.as_view(), name="postT"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('post/<int:pk>/remove', DeletePost.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
]
