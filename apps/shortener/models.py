import random
import string
from django.db import models
from django.utils import timezone

class ShortenerBaseModel(models.Model):
    """
    Abstract base model for the URL shortener app.
    Provides common fields for all models.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Make the BaseModel abstract

class Link(ShortenerBaseModel):
    """
    Represents a shortened URL link.
    """
    links = models.URLField()
    shorten_prefix = models.CharField(max_length=5, unique=True)
    expiration = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        Custom save method for the Link model.
        Sets the expiration time to 10 minutes from the current time when a new link is created.
        """
        if not self.pk:
            self.expiration = timezone.now() + timezone.timedelta(minutes=10)
        super().save(*args, **kwargs)

    def generate_unique_shorten_prefix(self):
        """
        Generates a unique shorten_prefix for the Link model.
        The shorten_prefix is a random 5-character string.
        """
        while True:
            new_prefix = ''.join(random.choices(string.ascii_letters, k=5))
            if not Link.objects.filter(shorten_prefix=new_prefix).exists():
                return new_prefix

    def clean(self):
        """
        Custom clean method for the Link model.
        Automatically generates a unique shorten_prefix if it's not provided.
        """
        if not self.shorten_prefix:
            self.shorten_prefix = self.generate_unique_shorten_prefix()
        super().clean()
