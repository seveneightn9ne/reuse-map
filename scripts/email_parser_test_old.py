from pprint import pprint

from emails.models import EmailMessage, EmailHeader


def test4():
    msg = EmailMessage.objects.get(id=223).get_email()
    print msg.get_payload()


def test3():
    msg = EmailMessage.objects.get(id=460).get_email()
    # print [part.get_content_type() for part in msg.walk()]
    # print msg['From']

    from_same = EmailMessage.objects.filter(emailheader__key="From", emailheader__value_short__contains="fracchia")
    for db_email in from_same:
        msg = db_email.get_email()
        part_types = [part.get_content_type() for part in msg.walk()]
        print msg['From']
        print part_types


def test2():
    table = {}

    for db_email in EmailMessage.objects.all():
        msg = db_email.get_email()
        part_types = [part.get_content_type() for part in msg.walk()]
        types_str = str(part_types)
        table[types_str] = table.get(types_str, 0) + 1

    pprint(table)


def test1():
    print 'hi'
    msg = EmailMessage.objects.get(id=415).get_email()
    print dir(msg)
    print [part.get_content_type() for part in msg.walk()]
    for part in msg.walk():
        print "----- ", part.get_content_type()
        raw_input()
        print part.get_payload()


test = test4
