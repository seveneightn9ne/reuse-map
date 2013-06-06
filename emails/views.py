from django.http import HttpResponse

import gather

def download_all_emails(request):
    gather.download_all_emails()
    return HttpResponse("Ok, I've downloaded the emails.")

def create_all_header_entries(request):
    gather.create_all_header_entries()
    return HttpResponse("Ok, I've created the header entries.")
