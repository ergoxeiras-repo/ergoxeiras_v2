from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Status(models.TextChoices):
    XYLOGLYPTH_FORHTH_EIKONA = 'xyloglypth-forhth-eikona', 'Ξυλόγλυπτη Φορητή Εικόνα'
    XYLOGLYPTH_KORNIZA = 'xuloglupth-korniza', 'Ξυλόγλυπτη Κορνίζα'
    PROETOIMASIA_EIKONAS = 'proetoimasia-eikonas', 'Προετοιμασία Εΐκόνας'
    KYTIA_LEIPSANOTHIKES = 'kytia-leipsanothikes', 'Κυτία Λειψανοθήκες'
    STAYROI = 'stauroi', 'Σταυροί'
    TRIPTYXA = 'triptyxa', 'Τρίπτυχα'
    BYZANTINA_MIKROGLYPTA = 'byzantina-mikroglypta', 'Βυζαντινά Μικρόγλυπτα'
    DIAFORES_KATASKEYES = 'diafores-kataskeyes', 'Διάφορες Κατασκευές'
    ERGA_PELATWN = 'erga-pelatwn', 'Έργα πελατών σε ξύλα μας'

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    category = models.CharField(max_length=32, choices=Status.choices) 
    uploaded_at = models.DateField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to='images')
    resized_image = ImageSpecField(
        source='image',
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.title
