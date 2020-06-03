from django.contrib import admin
from django.urls import path,include
from blog import views


urlpatterns=[
path('',views.PostList.as_view(),name='post_list'),
path('drafts/',views.PostDraftList.as_view(),name='drafts'),
path('about/',views.AboutView.as_view(),name='about'),
path('post/new/',views.CreatePost.as_view(),name='post_new'),
path('post/<pk>/',views.PostDetail.as_view(),name='post_detail'),
path('post/<pk>/update/',views.UpdatePost.as_view(),name='post_update'),
path('post/<pk>/delete/',views.DeletePost.as_view(),name='post_delete'),
path('post/<pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
path('post/<pk>/publish/',views.post_publish,name='post_publish'),
path('comments/<pk>/approve/',views.approve_comment,name='approve_comment'),
path('comments/<pk>/remove/',views.remove_comment,name='remove_comment'),
]
