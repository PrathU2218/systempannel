from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, first_name, mob_no, password=None):
        if not email:
            raise ValueError("User must have an email address!")

        if not first_name:
            raise ValueError("User must have first name!")


        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            mob_no = mob_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, mob_no, password=None):
        user=self.create_user(
            email = self.normalize_email(email),
            mob_no = mob_no,
            first_name = first_name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    """
    This is the custom user for our website.
    """
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, null=True, blank=True, default=None)
    email = models.EmailField(unique=True)
    mob_no = PhoneField(default=0000000000)
    prof_pic = models.ImageField(upload_to='prof_pics/', default=None)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'mob_no']

    objects = UserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
