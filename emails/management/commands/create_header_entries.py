from django.core.management.base import BaseCommand, CommandError

from emails import gather


class Command(BaseCommand):
    def handle(self, *args, **options):
        gather.create_all_header_entries()
