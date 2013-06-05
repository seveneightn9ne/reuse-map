from imapclient import IMAPClient

HOST = 'imap.mail.yahoo.com'
USERNAME = 'reusemap'
PASSWORD = 'xert-ra-wha-de'
ssl = True

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info['EXISTS'])

messages = server.search(['NOT DELETED'])
print("%d messages that aren't deleted" % len(messages))

print()
print("Messages:")
response = server.fetch(messages, ['FLAGS', 'RFC822'])
for msgid, data in response.iteritems():
    print('   ID %d: %s bytes, flags=%s' % (msgid,
                                            data['RFC822'],
                                            data['FLAGS']))
