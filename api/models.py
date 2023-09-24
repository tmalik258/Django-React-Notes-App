from django.db import models

# Create your models here.


class Note(models.Model):
    """Notes Model for adding any type of note or to do notes having a body field."""

    body = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Notes."""

        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        """Unicode representation of Notes."""
        return self.body[:50]
