from django.db import models


class Klub(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Jméno klubu', help_text="Enter a club's name")

    class Meta:
        verbose_name = 'Klub'
        verbose_name_plural = 'Kluby'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Fotbalista(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Jméno fotbalisty', help_text="Enter footballer's name")
    surname = models.CharField(max_length=50, unique=True, default='', verbose_name='Příjmení fotbalisty', help_text="Enter footballer's surname")
    birthDate = models.DateField(blank=True, null=True, verbose_name='Datum narození fotbalisty')
    description = models.CharField(max_length=500, null=True, verbose_name='Popis fotbalisty', help_text="Enter footballer's description")
    rate = models.IntegerField(verbose_name='Hodnocení fotbalisty', help_text="Enter a footballer's rating", null=True)
    poster = models.ImageField(verbose_name="Fotka fotbalisty", null=True)
    klub = models.ForeignKey(to="Klub", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = 'Fotbalista'
        verbose_name_plural = 'Fotbalisti'

    def __str__(self):
        return self.name
