from django.db import models


class Data(models.Model):
    a = models.IntegerField(verbose_name="Parameter a")
    b = models.IntegerField(verbose_name="Parameter b")
