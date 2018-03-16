from rest_framework import serializers
from usertimesheets.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model =  UserProfile
		fields = ('id','user','first_name','last_name','mobile','dob','gender','designation','is_delete','created_at','updated_at')
		extra_kwargs = {
			'first_name': {
				'required':True,
				'error_messages':{
				'required':"first name is required",
				}
			},
			'last_name': {
				'required':True,
				'error_messages':{
				'required':"last name is required"
				}
			},
			'mobile':{
				'required':False,
			},
			'dob':{
				'required':True,
				'error_messages':{
				'required':"dob is required",
				}
			},
			'gender':{
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			},
			'designation':{
				'required':True,
				'error_messages':{
				'required':"fill designation"
				}
			},

		}		