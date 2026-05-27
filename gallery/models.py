from django.db import models


class CarImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Car Images"

    def __str__(self):
        return self.title


class FlowerImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flowers/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Flower Images"

    def __str__(self):
        return self.title


class AnimalImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animals/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Animal Images"

    def __str__(self):
        return self.title