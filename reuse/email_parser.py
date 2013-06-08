import sys
import re

from emails.models import EmailMessage, EmailHeader


def test():
    parse_single_item_message(get_single_item_messages()[0])


def get_single_item_messages():
    return [
        EmailMessage.objects.get(uid=33, username='reusemap', host='imap.mail.yahoo.com'),
        EmailMessage.objects.get(uid=39, username='reusemap', host='imap.mail.yahoo.com'),
        EmailMessage.objects.get(uid=40, username='reusemap', host='imap.mail.yahoo.com'),
    ]


def extract_text(emailmessage):
    msg = emailmessage.get_email()
    plain_parts = filter(lambda part: part.get_content_type() == 'text/plain', msg.walk())
    full_text = reduce(lambda memo, part: memo + part.get_payload(), plain_parts, '')
    return full_text.replace('\r\n', '\n')


def print_with_invisibles(s):
    for char in s:
        if char == '\n':
            print '\\n'
        elif char == '\r':
            sys.stdout.write('\\r')
        else:
            sys.stdout.write(char)

def parse_single_item_message(emailmessage):
    full_text = extract_text(emailmessage)

    print_with_invisibles(full_text)

    print '\n' + '-' * 20 + '\n'

    location = re.search(r"E(.*)-(.*)th", full_text).groups()

    print 'location: ', location
