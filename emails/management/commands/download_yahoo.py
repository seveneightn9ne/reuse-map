from django.core.management.base import BaseCommand, CommandError

from emails import gather


class Command(BaseCommand):
    def handle(self, *args, **options):
        gather.download_all_emails()
