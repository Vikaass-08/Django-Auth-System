from django.conf.urls import  url
from passwordapp import views


app_name = 'passwordapp'

urlpatterns=[
   url('register/',views.register,name='register'),
   url('user_login/',views.user_login,name='user_login')

]
