import json
from django.shortcuts import HttpResponse

from models import ReuseObject


def _render_reuseobject(reuseobject):
    rendered = {}
    rendered['name']          = reuseobject.name
    rendered['details']       = reuseobject.details
    rendered['poster']        = reuseobject.poster
    rendered['building']      = reuseobject.building
    rendered['room']          = reuseobject.room
    rendered['count']         = reuseobject.count
    rendered['date_created']  = reuseobject.date_created.isoformat()
    rendered['date_modified'] = reuseobject.date_modified.isoformat()
    return rendered


def reuse_object(request):
    response_data = {}

    response_data['reuseobjects'] = map(_render_reuseobject, ReuseObject.objects.all())

    return HttpResponse(json.dumps(response_data), content_type="application/json")
