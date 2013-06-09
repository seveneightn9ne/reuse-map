import sys
import re
import itertools
from pprint import pprint

from emails.models import EmailMessage, EmailHeader

claimed = [
    "(.*)claimed",
    "claimed (.+)",
    "(.*)taken",
    "(.*)gone",
    "took (.+)"
]
not_claimed = [
    "(.+) not claimed",
    "(.+) still there",
    "(.+) remain",
    "(.+) remains",
    "(.+) not taken"
]
quantity = [
    "both",
    "all",
    "one",
    "a few"
]
bldg = "[^\w]([new]*\d\d?[newabcp]?)"
bldg_text = "b(?:ui)?ld(?:in)?g?"
room = bldg+"-[a-z]?\d\d\d?\d?"
places = [
    "("+bldg+" loading dock)",
    "(lobby \d+)",
    "(room "+room+")",
    "(outside (?:of)? "+room+")",
    "(\w+ floor (?:of)? "+bldg_text+" "+bldg+")",
    "("+bldg_text+" "+bldg+",? floor \w+)",
    "("+bldg_text+" "+bldg+",? \w+ floor)",
    "(.+ floor .+ .+)",
    "("+room+")",
    "("+bldg_text+" "+bldg+")",
    "("+bldg+"-\d\w\w floor)"
]


def test():
    parse_single_item_emailmessages(get_emailmessages())


def get_emailmessages():
    # q = []
    # for suid in range(1,40):
    #     q.append(EmailMessage.objects.get(uid=suid, username='reusemap', host='imap.mail.yahoo.com'))
    return EmailMessage.objects.all()
    # return [
    #     EmailMessage.objects.get(uid=33, username='reusemap', host='imap.mail.yahoo.com'),
    #     EmailMessage.objects.get(uid=39, username='reusemap', host='imap.mail.yahoo.com'),
    #     EmailMessage.objects.get(uid=40, username='reusemap', host='imap.mail.yahoo.com'),
    # ]


def extract_text(emailmessage):
    msg = emailmessage.get_email()
    plain_parts = filter(lambda part: part.get_content_type() == 'text/plain', msg.walk())
    full_text = reduce(lambda memo, part: memo + part.get_payload(), plain_parts, '')
    return full_text.replace('\r\n', '\n').replace("To sub/unsubscribe or to see the list rules:  http://mailman.mit.edu/mailman/listinfo/reuse","").replace("\n\n","\n")


def print_with_invisibles(s):
    for char in s:
        if char == '\n':
            print '\\n'
        elif char == '\r':
            sys.stdout.write('\\r')
        else:
            sys.stdout.write(char)


def parse_single_item_emailmessages(emailmessages):
    for emailmessage in emailmessages:
        print '\n' * 3 + '*' * 20 + '\n' * 3
        pprint(emailmessage)
        print '\n'
        result = parse_single_item_emailmessage(emailmessage)
        if 'location' in result:
            pprint(result)
        else:
            pprint(result)
            print "\n!! No location found in message"


def parse_single_item_emailmessage(emailmessage):
    full_text = extract_text(emailmessage)

    result = {}
    result['full_text'] = full_text

    for place in places:
        #print 'searching for '+place
        location_search = re.search(r""+place, full_text.lower())
        if location_search:
            result['location'] = location_search.groups()
            return result

    return result
