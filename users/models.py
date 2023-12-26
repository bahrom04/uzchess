from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from users import managers

class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone_number = CharField(
        max_length=32, null=True,blank=True, unique=True, error_messages={"unique": _("User already exists with that number")}
    )
    objects = managers.UserManager()

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username
