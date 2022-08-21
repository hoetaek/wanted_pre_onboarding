from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    area = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    position = models.CharField(max_length=128)
    payment = models.PositiveIntegerField()
    description = models.TextField()
    technology = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
