from django.db import models

class Category(models.Model):
    id_interno = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Curso(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return self.name