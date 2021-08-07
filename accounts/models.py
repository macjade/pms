from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
# Create your models here.

class DoctorManager(BaseUserManager):

    def create_user(self, username, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have a username")

        if not email:
            raise ValueError("User must have an email address")

        if not password:
            raise ValueError("User must have a password")

        user_obj = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, username, email, password=None):

        user_staff = self.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True
        )

        return user_staff

    def create_superuser(self, username, email, password=None):

        user_admin = self.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_admin=True
        )

        return user_admin

class Doctor(AbstractBaseUser, PermissionsMixin):

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=50, unique=True)
    hospital_name = models.CharField(max_length=255, default="SchoolProject")
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_of_joining = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = DoctorManager()

    def __str__(self):
        return str(self.username) + " - " + str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    def get_short_name(self):
        return self.firstname + " " + self.lastname

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

