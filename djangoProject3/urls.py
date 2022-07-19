"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sportapp import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', v.Register.as_view(), name='register'),
    path('login/', v.Login.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('home/', v.Home.as_view(), name='home'),
    path('', v.Home2.as_view(), name='home2'),
    path('update_profile/<int:pk>', v.UpdateProfile.as_view(), name='update'),
    path('delete_profile/<int:pk>', v.DeleteProfile.as_view(), name='account_delete'),
    path('posts/', v.PostsPage.as_view(), name='posts'),
    path('posts/<int:pk>', v.PostDetail.as_view(), name='post_detail'),
    path('edit_post/<int:pk>', v.EditPost.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', v.DeletePost.as_view(), name='delete_post'),
    path('events/', v.EventPage.as_view(), name='events_page'),
    path('event/<int:pk>', v.EventDetail.as_view(), name='event_detail'),
    path('add_post/', v.AddPost.as_view(), name='add_post'),
    path('add_event/', v.AddEvent.as_view(), name='add_event'),
    path('edit_event/<int:pk>', v.EditEvent.as_view(), name='edit_event'),
    path('delete_event/<int:pk>', v.DeleteEvent.as_view(), name='delete_event'),
    path('add_attendance/<int:pk>', v.AddEventAttendance.as_view(), name='add_atendance'),
    path('edit_attendance/<int:pk>', v.EditAttendance.as_view(), name='edit_attendance'),
    path('add_comment/<int:pk>', v.AddComment.as_view(), name='add_comment'),
    path('delete_comment/<int:pk>', v.DeleteComment.as_view(), name='delete_comment'),
    path('edit_comment/<int:pk>', v.EditComment.as_view(), name='edit_comment'),
    path('profile/<int:pk>', v.ProfilePage.as_view(), name='profile'),
    path('send_message/<int:id>', v.CreateMessage.as_view(), name='message'),
    path('inbox/', v.InboxView.as_view(), name='inbox'),
    path('delete_message/<int:pk>', v.DeleteMessage.as_view(), name='delete_comment'),
    path('add_group/', v.CreateGroup.as_view(), name='add_group'),
    path('join_group/<int:id>', v.JoinGroup.as_view(), name='join_group'),
    path('leave_group/<int:id>', v.LeaveGroup.as_view(), name='leave_group'),
    path('group_detail/<int:pk>', v.GroupDetail.as_view(), name='group_detail'),
    path('groups/', v.GroupsPage.as_view(), name='group_page'),
    path('delete_group/<int:pk>', v.DeleteGroup.as_view(), name='delete_group'),
    path('edit_group/<int:pk>', v.EditGroup.as_view(), name='edit_group'),

]
