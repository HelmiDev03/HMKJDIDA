from django.urls import path
from . import  views
urlpatterns=[
  
  path('', views.index, name='index'),

  path('removepost',views.removepost, name='removepost'),
  path('signup', views.signup, name='signup'),
  path('signin', views.signin, name='signin'),
  path('logout', views.logout, name='logout'),
  path('settings', views.settings, name='settings'),
  path('upload',views.upload, name='upload'),
  path('like-post', views.like_post, name='like-post'),
  path('follow', views.follow, name='follow'),
  path('profile/<str:pk>', views.profile, name='profile'),
  path('gotoprofile', views.gotoprofile, name='profile'),
  path('search', views.search, name='search'),
  path('testhome',views.testhome,name="testhome")
  #path is the url, views is the function in views.py, name is the name of the url





]