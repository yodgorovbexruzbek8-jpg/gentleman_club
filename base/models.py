from django.db import models


class Category(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Product(models.Model):
    kategoriya = models.ForeignKey(Category, on_delete=models.CASCADE)
    ism_familiya = models.CharField(max_length=200, blank=True, null=True)
    tajriba = models.PositiveIntegerField()
    reyting = models.FloatField(default=5.0)
    narx = models.PositiveIntegerField()
    tavsif = models.TextField(blank=True)

    def __str__(self):
        return self.ism_familiya


class Bron(models.Model):
    sartarosh = models.ForeignKey(Product, on_delete=models.CASCADE)
    mijoz_ismi = models.CharField(max_length=100)
    sana = models.DateField()
    vaqt = models.TimeField()

    def __str__(self):
        return self.mijoz_ismi