from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, date_of_birth, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            date_of_birth=date_of_birth,
            phone=phone,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, phone, password=None):
        user = self.create_user(email, date_of_birth, phone, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
