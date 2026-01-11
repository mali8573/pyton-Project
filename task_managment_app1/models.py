import enum

from django.contrib.auth.models import User
from django.db import models
from enum import Enum

class Team(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   def __str__(self):
      return self.name
class Role(models.TextChoices):
   ADMIN = 'ADMIN','Admin'
   WORKER = 'WORKER','Worker'
class Worker(models.Model):
   id = models.AutoField(primary_key=True)
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
   role=models.CharField(max_length=50,choices=Role.choices,default=Role.WORKER)
   phone = models.CharField(max_length=50)
   address = models.TextField()
   def __str__(self):
      return f"{self.user.username} {self.role}"
class TaskStatus(models.TextChoices):
      NEW = 'NEW','New'
      ACTIVE = 'ACTIVE','Active'
      FINISHED = 'FINISHED','Finished'
class Task(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   description = models.TextField()
   targetDate=models.DateField()
   status=models.CharField(max_length=50,choices=TaskStatus.choices,default=TaskStatus.NEW)
   operator=models.ForeignKey('Worker',on_delete=models.SET_NULL,null=True,blank=True)
   team=models.ForeignKey('Team',on_delete=models.SET_NULL,null=True,blank=True)
   def __str__(self):
      return f"{self.name} {self.status}"




