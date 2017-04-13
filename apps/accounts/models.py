from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        '''
        Base method for creating users.

        Args:
            email: (Required) User e-mail, which will be the `USERNAME_FIELD`.
            password: (Required) User password.
            **extra_fields: Extra fields.

        Returns:
            An instance of the created `user` object.
        '''
        if not email:
            raise ValueError('Email must not be empty')

        user = self.model(email=self.normalize_email(email),
                          date_joined=timezone.now(),
                          **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password, **extra_fields):
        # Create a normal user (is_staff=False, is_superuser=False).
        return self._create_user(email=email,
                                 password=password,
                                 is_staff=False,
                                 is_superuser=False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        # Create a super user (is_staff=True, is_superuser=True).
        return self._create_user(email=email,
                                 password=password,
                                 is_staff=True,
                                 is_superuser=True,
                                 **extra_fields)


class User(AbstractBaseUser):

    email = models.EmailField(_('Email Address'), unique=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email
