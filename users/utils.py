
from .models import User, UserRole
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from datetime import datetime
import logging

#create jwt token for a user
def auth_token(user):
    emp_id=User.objects.get(email=user.email).id
    access = AccessToken.for_user(user)
    refresh=RefreshToken.for_user(user)

    access['email']=user.email
    access['user_id']=emp_id
    refresh['email']=user.email
    refresh['user_id']=emp_id
    
    #sAVE LAST LOGIN TIME
    login_time = User.objects.filter(id=emp_id).update(last_login=datetime.now())
      
      
    return {"access_token": str(access),
    "refresh_token":str(refresh)}
    
    

    

def login_details(user):
    try:
        user_details = {}
        get_jwt = auth_token(user)
        user_details['access_token'] = get_jwt['access_token']
        user_details['refresh_token'] = get_jwt['refresh_token']
        user_details['email'] = user.email
        user_details['user_id'] = user.id
        user_details['user_name'] = user.username
   
        return user_details
        
    except Exception as e:
        logging.info(f"{e}: login details func")
        raise Exception
    
