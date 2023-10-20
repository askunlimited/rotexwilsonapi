from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError("Please enter a valid email address")

        if not first_name:
            raise ValueError("Please enter your first name")

        if not last_name:
            raise ValueError("Please enter your last name")

        if not phone:
            raise ValueError("Please enter your phone number")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, phone=phone
        )

        user.set_password(password)
        user.save()

        return user

    def create_vendor(self, email, first_name, last_name, phone, password=None):
        user = self.create_user(email, first_name, last_name, phone, password)

        user.is_vendor = True
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        user = self.create_user(email, first_name, last_name, phone, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    def __str__(self):
        return self.email
    
    
    def tokens(self):
        return ""
