from django.db import transaction
from imapclient import IMAPClient

from models import EmailMessage, EmailFlag

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
        response = self.server.fetch(uids, ['FLAGS', 'RFC822', 'RFC822.SIZE'])
        for msg_uid, data in response.iteritems():
            with transaction.commit_on_success():
                # extract data
                flags     = data['FLAGS']
                rfc_size = data['RFC822.SIZE']
                raw_body = data['RFC822']
                seq      = data['SEQ']

                # save objects
                email,_ = EmailMessage.objects.get_or_create(uid=msg_uid, raw_body=raw_body, rfc_size=rfc_size, seq=data['SEQ'])
                email.save()
                for flag in flags:
                    EmailFlag.objects.get_or_create(email=email, flag=flag)[0].save()

                # move message
                self.server.copy([msg_uid], 'auto_processed')
                self.server.delete_messages([msg_uid])
