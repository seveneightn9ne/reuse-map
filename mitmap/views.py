from django.shortcuts import redirect


def map(request):
    return redirect('/static/mitmap/reuse-map.html')
