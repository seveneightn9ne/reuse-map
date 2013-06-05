from django.http import HttpResponse

from client import EmailClient

def email_download(request):
  ec = EmailClient()
  ec.connect()
  ec.process_new_messages()
  return HttpResponse("Ok, I've downloaded the emails.")
