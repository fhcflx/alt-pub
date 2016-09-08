#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Francisco H C Felix'
SITENAME = u'Publicações acadêmicas'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
#        ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (
#         ('You can add links in your config file', '#'),
#         ('Another social link', '#'),
          ('google-plus', 'https://plus.google.com/u/0/+FranciscoHCFelix'),
          ('twitter', 'http://twitter.com/fhcflx'),
          ('github', 'http://github.com/fhcflx'),
          ('gitlab', 'http://gitlab.com/fhcflx'),
          ('bitbucket', 'http://bitbucket.org/fhcflx'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Specify name of a built-in theme
THEME = "mytheme"
