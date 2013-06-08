from django.core.management.base import BaseCommand, CommandError

from reuse import email_parser

class Command(BaseCommand):
    def handle(self, *args, **options):
        email_parser.test()
