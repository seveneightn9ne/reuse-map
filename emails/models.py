from django.db import models

class EmailMessage(models.Model):
    uid      = models.IntegerField(unique=True, db_index=True)
    raw_body = models.TextField()

class EmailTag(models.Model):
    email      = models.ForeignKey(EmailMessage, db_index=True)
    tag        = models.CharField(max_length=255, db_index=True)

    class Meta:
        unique_together = (('email', 'tag'),)
