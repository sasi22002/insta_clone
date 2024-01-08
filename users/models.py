from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,BaseUserManager
)

from utils.enum import GenderEnum
from django.contrib.auth.models import BaseUserManager

from django.db import transaction
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise Exception('Model creation Error')

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password=password, **extra_fields)

class Role(models.Model):
    """
    User roles
    1 - ADMIN
    2 - USER

    Args:
        models (_type_):user roles
    """
    role_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default= True)
    class Meta:
        db_table = 'role_master'
        

# User related tables
class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """
    email = models.EmailField(max_length=126, unique=True,null = False)
    username = models.CharField(max_length =60)
    password = models.CharField(max_length=256,null = True,blank = True)
    phone_number=models.CharField(max_length=128,null=True,unique=True)
    address = models.CharField(max_length=256,null = True)
    gender = models.CharField(max_length=8,default=GenderEnum.Not_to_say.value,blank=True,null=True)
    is_block = models.BooleanField(default= False)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True,null = True)
    updated_at = models.DateTimeField(auto_now=True,null = True)   
    last_login = models.DateTimeField(blank=True,null=True)
    is_deleted= models.BooleanField(default=False)
   

    class Meta:
        db_table = 'auth_master'

    objects = UserManager()

    USERNAME_FIELD = 'email'

    
   

class UserActivityLog(models.Model):
    """
    MODEL FOR MAINTAIN USER ACTIVITY
    """
    user=models.ForeignKey(User,related_name='user_activity',null=True,on_delete=models.CASCADE)
    activity_details = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null = True)
    updated_at = models.DateTimeField(auto_now=True,null = True)
              
    class Meta:
        db_table = 'activity_log'


class UserRole(models.Model):
    """
    Args:
        models : Model for mapping user with respective roles
    """
    role = models.ForeignKey(Role,on_delete=models.CASCADE,related_name='user_role',null = True,blank=True)
    user=models.ForeignKey(User,related_name='userrole_user',null=True,on_delete=models.CASCADE)
    is_active = models.BooleanField(default= True)
    
    class Meta:
        db_table = 'user_roles'
        
        
        

class UserSession(models.Model):
    """
    MODEL FOR MAINTAIN USER SESSIONS
    """
    access_token = models.TextField()
    refresh_token = models.TextField(null=True)
    auth=models.ForeignKey(User,related_name='auth_session',null=True,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    sessiontext = models.TextField(max_length=220)
    loggedin_as = models.IntegerField(null=True)


    class Meta:
        db_table = 'user_session'
        


class FollowRequest(models.Model):
    """
    MODEL FOR MAINTAIN USER FOLLOW REQUESTS
    """
    user=models.ForeignKey(User,related_name='user',null=False,on_delete=models.CASCADE)
    following_user = models.ForeignKey(User,related_name='user_follow',null=False,on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null = True)
    updated_at = models.DateTimeField(auto_now=True,null = True)
    
    class Meta:
        db_table = 'follow_request'

