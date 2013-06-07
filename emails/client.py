from django.db import transaction
from imapclient import IMAPClient
from getpass import getpass

from models import EmailMessage, EmailFlag


def email_configs(which):
    if which is 'yahoo':
        return {
            'HOST':     'imap.mail.yahoo.com',
            'USERNAME': 'reusemap',
            'PASSWORD': 'xert-ra-wha-de',
            'USE_SSL':  True,
        }
    elif which is 'gmail':
        return {
            'HOST':     'imap.gmail.com',
            'USERNAME': raw_input("Enter gmail account (with @gmail.com): "),
            'PASSWORD': getpass("Enter gmail password: "),
            'USE_SSL':  True,
            'FOLDER':   'reuse',
        }


class EmailClient(object):
    def __init__(self, config):
        """
        Create an email client abstraction configured for an account.

        config is a dict with keys:
            HOST
            USERNAME
            PASSWORD
            USE_SSL default=True
            FOLDER default='INBOX'
            SELECTORS default=['NOT DELETED']
        """
        self.config = {'USE_SLL': True, 'FOLDER': 'INBOX', 'SELECTORS': ['NOT DELETED']}
        self.config.update(config)

    def connect(self):
        self.server = IMAPClient(self.config['HOST'], use_uid=True, ssl=self.config['USE_SSL'])
        self.server.login(self.config['USERNAME'], self.config['PASSWORD'])
        select_info = self.server.select_folder(self.config['FOLDER'])

    def process_new_messages(self, debug=False):
        """
        Get mesages from the server.

        Note: new information on existing uids will be ignored.
        For example, if the rfc_size changes (which is a strangely common occurrence),
        the new value will be ignored.
        """
        if debug: print "searching"
        messages = self.server.search(self.config['SELECTORS'])
        if debug: print "done searching"
        self._process_messages(messages, debug=debug)

    def _process_messages(self, uids, move=False, debug=False):
        if debug: print "fetching"
        response = self.server.fetch(uids, ['FLAGS', 'RFC822', 'RFC822.SIZE'])
        for msg_uid, data in response.iteritems():
            if debug: print "processing %s" % msg_uid
            with transaction.commit_on_success():
                # extract data
                flags    = data['FLAGS']
                rfc_size = data['RFC822.SIZE']
                raw_body = data['RFC822']
                seq      = data['SEQ']

                # save objects
                email, _ = EmailMessage.objects.get_or_create(
                    uid      = msg_uid,
                    username = self.config['USERNAME'],
                    host     = self.config['HOST'],
                    defaults = {
                        'raw_body': raw_body,
                        'rfc_size': rfc_size,
                        'seq':      data['SEQ'],
                    } )

                email.save()

                for flag in flags:
                    EmailFlag.objects.get_or_create(email=email, flag=flag)[0].save()

                # move message
                if move:
                    self.server.copy([msg_uid], 'auto_processed')
                    self.server.delete_messages([msg_uid])
