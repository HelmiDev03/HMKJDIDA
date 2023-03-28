from django.contrib.auth import views as authViews
from . import  views
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy






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
  path('search', views.search, name='search'),]
  #path is the url, views is the function in views.py, name is the name of the url
#password reset via email


  


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns += [
    path('reset_password/', authViews.PasswordResetView.as_view(template_name= "registration/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', authViews.PasswordResetDoneView.as_view(template_name= "registration/password_reset_sent.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'), 
    path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view(template_name= "registration/password_reset_done.html"), name="password_reset_complete"),
    path('password-reset/', 
     PasswordResetView.as_view(
        template_name='users/password_reset.html',
        html_email_template_name='users/password_reset_email.html'
    ),
    name='password-reset'
),
    ]

