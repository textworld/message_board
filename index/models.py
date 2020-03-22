from django.db import models


# 基础模型
class CommonInfo(models.Model):
    gmt_update = models.DateTimeField(auto_now=True, null=True, blank=True)
    gmt_create = models.DateTimeField(auto_created=True, null=True, blank=True)

    class Meta:
        abstract = True


class Message(CommonInfo):
    username = models.CharField(max_length=64)
    content = models.TextField(max_length=65535)

    def __str__(self):
        return f'{self.username}: {self.content}'
