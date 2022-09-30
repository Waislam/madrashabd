from datetime import date
from django.db import models
from accounts.models import Madrasha


# Create your models here.
BOOK_CATEGORY = (('nesabi', 'Nesabi'),
               ('hadis/usolehadis', 'Hadis/Usolehadis'),
               ('fekah/usolefekhan', 'Fekah/Usolefekhan'),
               ('tafsir', 'Tafsir'),
               ('mantek', 'Mantek'),
               ('quran', 'Quran'),
               ('quran', 'Quran'),
               ('akida', 'Akida'),
               ('etihash', 'Etihash'),
               ('orthoniti', 'Orthoniti'),
               ('vugol', 'Vugol'),
               ('arbi shahitto', 'Arbi shahitto'),
               ('nahu', 'Nahu'),
               ('sorof', 'Sorof'),
               ('sirat', 'Sirat'),
               ('eslah', 'Eslah'),
               ('ovidhan', 'Ovidhan'),
               ('golpo shahitto', 'Golpo shahitto'),
               ('fatwa', 'Fatwa'),
               ('ralagad', 'Balagad'),
               ('rasayel', 'Rasayel'),
               ('other', 'Other'),
               )


class LibraryBook(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, related_name='library_books', null=True, blank=True)
    number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    part = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, choices=BOOK_CATEGORY, default='Hadis')
    book_for_class = models.CharField(max_length=100, blank=True, null=True)
    translator = models.CharField(max_length=100, blank=True, null=True)
    publication = models.CharField(max_length=100, blank=True, null=True)
    original_writer = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name

