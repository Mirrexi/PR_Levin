from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateTimeField()
    desc = models.TextField()

    def __str__(self):
        return self.title  # Иначаче при обращение к title будет объект