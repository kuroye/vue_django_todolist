from pyexpat import model
from statistics import mode
from django.db import models
from ability.models import Ability
from user.models import MyUser
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, null=False)
    is_finished = models.BooleanField(default=False)
    subject = models.ManyToManyField(Ability)
    dodo = models.IntegerField()

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
