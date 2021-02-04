from django.db import models


class Department(models.Model):
    dep_name = models.CharField(max_length=100, default=None, unique=True)
    test_field = models.IntegerField(default=None, null=True)

    def __str__(self):
        return "{}".format(self.dep_name)
