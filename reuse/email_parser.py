import sys
import re
import itertools
from pprint import pprint
from django.db.models import Q

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
bldg = "([new]*\d\d?[newabcp]?)"
bldg_text = "b(?:ui)?ld(?:in)?g?"
room = bldg+"-[a-z]?\d\d\d?\d?"
nth_floor = "\d\w\w floor"
places = [
    "("+bldg+" loading dock)",
    "(lobby (\d+))",
    "(room "+room+")",
    "(outside (?:of)? "+room+")",
    "("+nth_floor+" (?:of)? "+bldg_text+" "+bldg+")",
    "("+bldg_text+" "+bldg+",? floor \w+)",
    "("+bldg_text+" "+bldg+",? "+nth_floor+")",
    "("+room+")",
    "("+bldg_text+" "+bldg+")",
    "("+bldg+"-"+nth_floor+")",
    "("+nth_floor+" \w+ \w+)()"
]
no_places = [
    "(inter[ -]?office (?:(?:address)|(?:mail)))"
]


def test():
    parse_single_item_emailmessages(get_emailmessages())
    # parse_single_item_emailmessages(get_emailmessages()[0:1])


def get_emailmessages():
    # return EmailMessage.objects.filter(id=120)
    return EmailMessage.objects.filter(Q(emailheader__key='To', emailheader__value__contains='reuse@mit.edu')|
                                       Q(emailheader__key='Cc', emailheader__value__contains='reuse@mit.edu')).all()
    #return EmailMessage.objects.filter(emailheader__key='To',emailheader__value__regex=r'^((?!reusemap@yahoo.com).*)$')
    # return EmailMessage.objects.all()


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
        pprint(result)
        if not ('location' in result or 'noplace' in result):
            print "\n!! No location found in message"


def parse_single_item_emailmessage(emailmessage):
    full_text = extract_text(emailmessage)
    lower_text = full_text.lower()

    result = {}
    # result['full_text'] = full_text[:100] if len(full_text)>102 else full_text
    # result['full_text'] = full_text
    result['-lower_text'] = lower_text

    for no_place in no_places:
        location_search = re.search(r""+no_place, lower_text)
        if location_search:
            result['noplace'] = True
            return result

    for place in places:
        #print 'searching for '+place
        location_search = re.search(r"(?:^|\W)"+place, lower_text)
        if location_search:
            print "matched "+place

            building = location_search.groups()[0]
            # TODO remove this if statement when places gaurantees two capture groups
            if len(location_search.groups()) > 1:
                room = location_search.groups()[1]
            else:
                room = None

            result['location'] = {
                'building': building,
                'room': room,
            }
            return result

    return result
