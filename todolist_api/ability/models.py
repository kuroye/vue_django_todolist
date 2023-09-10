from django.db import models
from user.models import MyUser
# Create your models here.

# 一个Group里有好多Ability 每个用户的都不同 所以需要user外键
class AbilityGroup(models.Model):

    name = models.CharField(max_length=150, null=False, blank=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# Ability代表用户能力 需要Group外键 Group外键=user外键 
# 就算多个用户的Ability名字重复了 group使它特殊
class Ability(models.Model):

    subject = models.CharField(max_length=150, null=False, blank=False)
    score = models.FloatField(default=0)

    group = models.ForeignKey(AbilityGroup, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return str(self.group) +  ' | ' + str(self.subject)