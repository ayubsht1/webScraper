from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=255)
    date_scraped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title