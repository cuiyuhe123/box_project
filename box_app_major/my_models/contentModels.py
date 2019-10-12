from django.db import models


class contnet(models.Model):
        content_name = models.CharField(max_length=100)
        content_describe = models.TextField(null=True)
        content_url = models.TextField(null=True)
        content_color = models.CharField(max_length=20,null=True)
        