from django.db import models


class ReuseObject(models.Model):
    short    = models.CharField(max_length=255, db_index=True)
    details  = models.TextField(blank=True, null=True)
    poster   = models.EmailField(max_length=254)
    building = models.CharField(max_length=255, db_index=True, blank=True, null=True)
    room     = models.CharField(max_length=255, db_index=True, blank=True, null=True)
    count    = models.IntegerField(default=1)

    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)
