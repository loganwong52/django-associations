from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, default="")

# actor can be in many movies
# movies have many actors
# many to many attribute, so ONE of the classes needs the attribute. Doesn't matter which.

class Actor(models.Model):
    name = models.CharField(max_length=64, default="")
    movies = models.ManyToManyField(Movie, related_name="actors", through="Role")
# related_name is how the opposite side of the relationship refers to this data
# If I'm creating a field in THIS model, the related name should be the same as THIS model, but plural

# You need through="Roles" to explicitly make Role the join table for Movie and Actor. 
# Without it, Django will create it's own join table, instead of using Role.

# This is like a join table
class Role(models.Model):
    # 1 to many
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
    # This makes a realted_name attribute in Actor called roles
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")
    # This makes a realted_name attribute in Movies called roles
