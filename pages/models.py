from django.db import models

class Status(models.TextChoices):
    IMAGE_PERPERATION = 'proetimasia-eikonas', 'Προετοιμασία Εικόνας'
    WOOD_CARVED_IMAGE = 'xuloglupth-eikona', 'Ξυλόγλυπτη Εικόνα'
    IMAGE_FRAME = 'korniza', 'Κορνίζα'

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    category = models.CharField(max_length=32, choices=Status.choices) 
    uploaded_at = models.DateField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
