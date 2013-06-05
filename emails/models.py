from django.db import models
import email

class EmailMessage(models.Model):
    uid      = models.IntegerField(unique=True, db_index=True)
    raw_body = models.TextField()
    rfc_size = models.IntegerField(db_index=True, null=True)
    seq      = models.IntegerField(blank=True, null=True)

    def get_email(self):
      # TODO email.message_from_string can't handle unicode. Is that an issue?
      return email.message_from_string(str(self.raw_body))

class EmailFlag(models.Model):
    email      = models.ForeignKey(EmailMessage, db_index=True)
    flag        = models.CharField(max_length=255, db_index=True)

    class Meta:
        unique_together = (('email', 'flag'),)
