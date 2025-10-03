from django.db import models
from django.conf import settings


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Petition(models.Model):
    """A user-submitted petition to request adding a movie to the catalog.

    Fields:
    - title: Short title (e.g. movie name)
    - description: Optional rationale/details
    - created_by: optional FK to User (nullable for anonymous)
    - created_at: timestamp
    - voters: M2M to User storing who voted for the petition
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='petitions')
    created_at = models.DateTimeField(auto_now_add=True)
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='voted_petitions')

    def votes_count(self):
        return self.voters.count()

    def __str__(self):
        return f"Petition: {self.title} ({self.votes_count()} votes)"

