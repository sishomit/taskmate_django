from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from django.utils import timezone


# Create your models here.


class Tasklist(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    task_deadline = models.DateTimeField(auto_now=False, default=None)
    current_time = models.DateTimeField(auto_now_add=True)

    def is_deadline_over(self):
        timenow = localtime()
        deadtime = self.task_deadline

        if timenow > deadtime:
            return True

    def __str__(self):
        return self.task


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " -" + str(self.time)
