from django.contrib.auth.models import BaseUserManager
from django.utils import timezone



class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extrafields):
        if not email:
            raise ValueError('User Must Have Email')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extrafields
        )

# set password
        user.set_password(password)
        user.ssave(using=self._db)
        return user

#create data user
    def create_user(self, email, password, **extra_field):
        return self._create_user(email, password, False, False, **extra_field)

    def create_superUser(self, email, password, **extra_field):
        user = self._create_user(email, password, True, True, **extra_field)
        user.save(using=self.db)
        return user
