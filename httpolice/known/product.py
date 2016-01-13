# -*- coding: utf-8; -*-

from httpolice.common import ProductName
from httpolice.known.base import KnownDict


def is_library(name):
    return known.get_info(name).get('library')


known = KnownDict([
 {'_': ProductName(u'android-async-http'),
  'library': True},
 {'_': ProductName(u'Apache-HttpAsyncClient'),
  'library': True},
 {'_': ProductName(u'Apache-HttpClient'),
  'library': True},
 {'_': ProductName(u'CFNetwork'),
  'library': True},
 {'_': ProductName(u'Dalvik'),
  'library': True},
 {'_': ProductName(u'Darwin'),
  'library': True},
 {'_': ProductName(u'Go-http-client'),
  'library': True},
 {'_': ProductName(u'Java'),
  'library': True},
 {'_': ProductName(u'libcurl'),
  'library': True},
 {'_': ProductName(u'libidn'),
  'library': True},
 {'_': ProductName(u'libsoup'),
  'library': True},
 {'_': ProductName(u'libwww-perl'),
  'library': True},
 {'_': ProductName(u'OpenSSL'),
  'library': True},
 {'_': ProductName(u'PHP'),
  'library': True},
 {'_': ProductName(u'php-requests'),
  'library': True},
 {'_': ProductName(u'PycURL'),
  'library': True},
 {'_': ProductName(u'python-requests'),
  'library': True},
 {'_': ProductName(u'Python-urllib'),
  'library': True},
 {'_': ProductName(u'zlib'),
  'library': True},
], extra_info=['library'])