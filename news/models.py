from django.db import models
from django.shortcuts import reverse

class New(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def get_detail_url(self):
        return reverse('news:detail', args=[self.pk])