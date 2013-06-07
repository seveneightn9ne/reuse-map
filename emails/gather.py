"""
Utilities for gathering and loading emails
"""

from models import EmailMessage
from client import EmailClient, email_configs

def download_all_emails():
    ec = EmailClient(email_configs('yahoo'))
    ec.connect()
    ec.process_new_messages()

def create_all_header_entries():
    for em in EmailMessage.objects.all():
        em.create_header_entries()
