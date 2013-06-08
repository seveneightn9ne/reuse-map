from django.core.management.base import BaseCommand, CommandError

from emails.client import EmailClient, email_configs


class Command(BaseCommand):
    def handle(self, *args, **options):
        ec = EmailClient(email_configs('gmail'))
        print "connecting"
        ec.connect()
        print "processing new messages"
        ec.process_new_messages(debug=True)
