from django.db import models
from django.utils.text import slugify

# Create your models here.

choices = (('Comedy', 'Comedy'),
           ('Drama', 'Drama'), 
           ('Action', 'Action'),
           ('Horror', 'Horror'),
           ('Sci-Fi', 'Sci-Fi'))

class MovieDetails(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_category = models.CharField(choices=choices, max_length=30)
    cost = models.IntegerField()
    trailer_link = models.URLField()
    slug = models.CharField(max_length=50, editable=False)
    
    def __str__(self):
        return self.movie_name
    
    def save(self, *args, **kwargs):
        super(MovieDetails, self).save()
        self.slug = slugify(self.movie_name)
        super(MovieDetails, self).save()