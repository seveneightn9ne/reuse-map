from getpass import getpass
from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = 'mlsteele00@gmail.com'
PASSWORD = getpass()
ssl = True

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

select_info = server.select_folder('reuse')
print('%d messages in INBOX' % select_info['EXISTS'])

messages = server.search(['NOT DELETED'])
print("%d messages that aren't deleted" % len(messages))

print()
print("Messages:")
response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
for msgid, data in response.iteritems():
    print('   ID %d: %s bytes, flags=%s' % (msgid,
                                            data['RFC822.SIZE'],
                                            data['FLAGS']))
