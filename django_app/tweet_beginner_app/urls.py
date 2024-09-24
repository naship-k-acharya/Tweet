from django.urls import path
from . import views



urlpatterns = [
    path('', views.tweet_list, name = 'tweet_list'),
    path('create/', views.tweet_create, name = 'tweet_create'),
    path('friend_request/', views.friend_request, name = 'friend_request'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name = 'tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name = 'tweet_delete'),
    path('register/', views.register, name='register'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like'),
    path('tweet/<int:tweet_id>/comments',views.comment_tweet,name='add_comment'),
    path('send-friend-request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept-friend-request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('delete-friend-request/<int:request_id>/', views.delete_friend_request, name='delete_friend_request'),
]

