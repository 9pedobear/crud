from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Сотрудники'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'