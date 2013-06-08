from django.shortcuts import render, redirect


def map(request):
    return redirect('/static/mitmap/reuse-map.html')


def google_map(request):
    return render(request, 'mitmap/google_map.html', {})
