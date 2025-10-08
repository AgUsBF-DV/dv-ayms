from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import TimeStampedModel


class Role(TimeStampedModel):
    name = models.CharField(max_length=32, unique=True, verbose_name="Role Name")
    visible = models.BooleanField(default=True, verbose_name="Visible")

    class Meta:
        ordering = ['name']
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    firstName = models.CharField(max_length=80, verbose_name="First Name")
    lastName = models.CharField(max_length=80, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="Role")
    isActive = models.BooleanField(default=True, verbose_name="Active")
    visible = models.BooleanField(default=True, verbose_name="Visible")

    class Meta:
        ordering = ['lastName', 'firstName']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.username} ({self.email})"


class Customer(TimeStampedModel):
    firstName = models.CharField(max_length=80, verbose_name="First Name")
    lastName = models.CharField(max_length=80, verbose_name="Last Name")
    email = models.EmailField(null=True, blank=True, unique=True, verbose_name="Email Address")
    visible = models.BooleanField(default=True, verbose_name="Visible")

    class Meta:
        ordering = ['lastName', 'firstName']
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
