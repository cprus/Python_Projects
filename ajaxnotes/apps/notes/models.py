from __future__ import unicode_literals

from django.db import models

class notes(models.Model):
    name = models.CharField(max_length = 255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
