from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE = (
        ("own", "Owner"),
        ("su", "Superuser"),
        ("rdr", "Reader"),
    )
    _type = models.CharField(max_length=3, choices=USER_TYPE, default="own")

    @property
    def allow_create(self) -> bool:
        return self._type == "su"

    @property
    def allow_read(self) -> bool:
        return True

    @property
    def allow_update(self) -> bool:
        return self._type == "own"

    @property
    def allow_delete(self) -> bool:
        return False  # ?

    def __str__(self):
        return f"{self.email} ({self._type.upper()})"
