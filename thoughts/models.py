from django.db import models


class Thought(models.Model):
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Thought"
        verbose_name_plural = "Thoughts"

    def __str__(self):
        return self.description
