from .custom import get_unique_reference
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    # Overwriting to make name fields required
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)

    # Replacing username with email
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Claim(models.Model):
    creation_datetime = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    reference = models.CharField(max_length=8, default="0")

    @classmethod
    def create(cls, owner, description):
        now = timezone.now()
        reference = get_unique_reference(cls, "C")
        claim = cls(owner=owner, description=description, creation_datetime=now, reference=reference)
        return claim

    def user_can_access(self, user):
        return self.owner == user


class Receipt(models.Model):
    CATEGORIES = [
        ("ML", "Meal"),
        ("TI", "Taxi"),
    ]
    claim = models.ForeignKey("Claim", on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    vat = models.FloatField()
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    date_incurred = models.DateField()
