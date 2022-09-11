from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# from django.http.request import RAISE_ERROR

# Create your models here.
class myAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an emailaddress')
        if not username:
            raise ValueError('User must have an username')

        user= self.model(
            email= self.normalize_email(email),
            username= username,
            first_name= first_name,
            last_name= last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user=self.create_user(
            email       =self.normalize_email(email),
            username    =username,
            password    =password,
            first_name  =first_name,
            last_name   =last_name,
        )
        user.is_admin= True
        user.is_active= True
        user.is_agent= True
        user.is_staff= True
        user.is_superadmin= True
        user.save(using=self._db)
        



class Account(AbstractBaseUser, PermissionsMixin):
    SUPER_ADMIN = 1
    BUS_VENDOR = 2
    HOTEL_VENDOR = 3
    CUSTOMER = 4

    ROLE_CHOICE = (
        (SUPER_ADMIN, 'Admin'),
        (BUS_VENDOR, 'Bus'),
        (HOTEL_VENDOR, 'Hotel'),
        (CUSTOMER, 'Customer'),
    )

    first_name      =models.CharField(max_length=50)
    last_name       =models.CharField(max_length=50)
    username        =models.CharField(max_length=50, unique=True)
    email           =models.EmailField(max_length=100, unique=True)
    phone_number    =models.CharField(max_length=100)
    role            = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    #required

    date_joined     =models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(auto_now_add=True)
    is_admin        =models.BooleanField(default=False)
    is_staff        =models.BooleanField(default=False)
    is_verified        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=False)
    is_superadmin   =models.BooleanField(default=False)


    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS =['username', 'first_name', 'last_name']

    objects = myAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Admin'
        elif self.role == 2:
            user_role = 'Bus'
        elif self.role ==3:
            user_role = 'Hotel'
        elif self.role ==3:
            user_role = 'Customer'
        return user_role
