from django.urls import path
from users import views


urlpatterns = [
    path('user_follow',views.FollowUserRequest.as_view(),name='user_follow'),
    path('user_list',views.UserList.as_view(),name='user_list'),
    path('friend_list',views.FriendList.as_view(),name='friend_list'),

       
    ]
    