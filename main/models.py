from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from main.managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.TextField(blank=False)
    phone = models.CharField(unique=True, max_length=15)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth", "phone"]

    def __str__(self):
        return self.email


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Trainer(models.Model):
    user = models.ForeignKey(User(models.Model), on_delete=models.CASCADE)
    kyc_option = models.CharField(max_length=100)
    kyc = models.ImageField()
    kyc_approved = models.BooleanField()
    basic_salary = models.IntegerField()


class Trainee(models.Model):
    user = models.ForeignKey(User(models.Model), on_delete=models.CASCADE)
    kyc_option = models.CharField(max_length=100)
    kyc = models.ImageField()
    kyc_approved = models.BooleanField()


class Programme(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    trainers = models.ManyToManyField(Trainer, through="TrainerProgramme")


class TrainerProgramme(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    commission = models.IntegerField()
