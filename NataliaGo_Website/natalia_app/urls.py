from django.urls import include,path,re_path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('writer/',views.writer,name='writer'),
    path('actor/',views.actor,name='actor'),

    ##from udemy tutorial
    path('about/',views.AboutView.as_view(),name='about'),
    path('post_list/',views.PostListView.as_view(),name='post_list'),

    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new_post/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),

    path('post/<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_confirm_delete'),

    path('drafts/',views.DraftListView.as_view(),name='drafts_view'),

    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
]
