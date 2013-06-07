from django.db import models
import email


# TODO watch out for duplicate messages with different uids (e.g. moved messages)
class EmailMessage(models.Model):
    uid      = models.IntegerField(db_index=True)
    username = models.CharField(max_length=255, db_index=True)
    host     = models.CharField(max_length=255, db_index=True)
    raw_body = models.TextField()
    rfc_size = models.IntegerField(db_index=True, null=True)
    seq      = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = (('uid', 'username', 'host'))

    def get_email(self):
        # TODO email.message_from_string can't handle unicode. Is that an issue?
        return email.message_from_string(str(self.raw_body))

    def create_header_entries(self):
        for (key, value) in self.get_email().items():
            EmailHeader.objects.get_or_create(
                email = self,
                key   = key,
                defaults={
                    'value_short': value[:254],
                    'value':       value,
                } )


class EmailFlag(models.Model):
    email = models.ForeignKey(EmailMessage, db_index=True)
    flag  = models.CharField(max_length=255, db_index=True)

    date_created  = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = (('email', 'flag'),)


class EmailHeader(models.Model):
    email       = models.ForeignKey(EmailMessage, db_index=True)
    key         = models.CharField(max_length=255, db_index=True)
    value_short = models.CharField(max_length=255, db_index=True)
    value       = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = (('email', 'key'))
