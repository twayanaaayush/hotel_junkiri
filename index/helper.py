import urllib
from django.urls import reverse


def url_builder(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urllib.parse.urlencode(get)
    return url