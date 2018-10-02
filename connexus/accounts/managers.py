from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=True, is_admin=True):
        if not email:
            raise ValueError("Users must have email address")
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active

        user.save(using=self._db)

        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )

        return user
