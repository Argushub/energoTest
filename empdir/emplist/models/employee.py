from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    second_name = models.CharField(max_length=50, default=None)
    patronymic = models.CharField(max_length=50, default=None)
    position = models.CharField(max_length=200, default=None)
    tel_number = models.CharField(max_length=12, default=None)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to="emplist/media", default=None)
    department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        unique_together = ['first_name', 'second_name', 'patronymic', 'birth_date']

    def __str__(self):
        return "{} {} {} {}".format(self.second_name, self.first_name, self.patronymic, self.birth_date)
