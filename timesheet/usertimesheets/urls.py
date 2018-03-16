from django.conf.urls import url,include
from . import views
app_name='usertimesheet'


urlpatterns = [
	url(r'^(?P<user_id>[0-9]+)$',views.UserProfileList.as_view()), 
	url(r'',views.UserProfileList.as_view()), 
	# url(r'^(?P<user_id>[0-9]+)$',views.UpdateUserProfile.as_view()),
]
