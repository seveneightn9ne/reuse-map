from imapclient import IMAPClient

from models import EmailMessage

class EmailClient(object):
    def __init__(self):
        self.config = {
            'HOST':     'imap.mail.yahoo.com',
            'USERNAME': 'reusemap',
            'PASSWORD': 'xert-ra-wha-de',
            'USE_SSL':  True    ,
        }

    def connect(self):
        self.server = IMAPClient(self.config['HOST'], use_uid=True, ssl=self.config['USE_SSL'])
        self.server.login(self.config['USERNAME'], self.config['PASSWORD'])
        select_info = self.server.select_folder('INBOX')

    def process_new_messages(self):
        messages = self.server.search(['NOT DELETED'])
        self._process_messages(messages)

    def _process_messages(self, uids):
        response = self.server.fetch(uids, ['RFC822'])
        for msg_uid, data in response.iteritems():
            raw_body = data['RFC822']
            EmailMessage.objects.create(uid=msg_uid, raw_body=raw_body)
