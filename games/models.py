from django.db import models

# Create your models here.
class Videogame(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    release_date = models.DateField()

    # metodo speciale per restituire il campo che vogliamo 
    def __str__(self) -> str:
        return self.title