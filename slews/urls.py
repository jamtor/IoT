from django.conf.urls import url
from slews import views

app_name = 'slews'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^main/$',views.main,name='main'),
    url(r'^dashboardslews/$',views.dashboard,name='dashboard')
]
