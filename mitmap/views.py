from django.http import HttpResponse
from django.conf import settings

def list_urls(request):
  print settings.urlpatterns
  return HttpResponse("Hello.")
