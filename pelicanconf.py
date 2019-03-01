#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Francisco H C Felix'
SITENAME = u'Academic publications'
SITEURL = 'http://fhcflx.github.io/alt-pub'

PATH = 'content'
OUTPUT_PATH = 'public'
STATIC_PATHS = [
    'extra',
    'images',
    'pdf'
    ]
EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/android-chrome-256x256.png': {'path': 'android-chrome-256x256.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon.32x32.png': {'path': 'favicon-32x32.png'},
    'extra/mstile-150x150.png': {'path': 'mstile150x150.png'},
    'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
    # 'extra/htaccess': {'path': '.htaccess'}
    }

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ciência Médica', 'http://fhcflx.github.io/ciencia-medica/'),
         ('Pharmakon', 'http://pharmak.blogspot.com/'),
         ('Neuro-oncologia', 'http://fhcflx.github.io/cpc-neuro/'),
#         ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (
#         ('You can add links in your config file', '#'),
#         ('Another social link', '#'),
          ('linkedin', 'https://www.linkedin.com/in/francisco-h-c-felix-84ba8226?trk=hp-identity-name'),
          ('twitter', 'http://twitter.com/fhcflx'),
          ('github', 'http://github.com/fhcflx'),
#         ('gitlab', 'http://gitlab.com/fhcflx', 'Gitlab'),
#         ('bitbucket', 'http://bitbucket.org/fhcflx'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Specify name of a built-in theme
THEME = "themes/pelican-bootstrap3"

import os
import sys
sys.path.append(os.curdir)
from themeconf import *

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    # 'code_include',
    # 'series',
    # 'related_posts',
    # 'better_codeblock_line_numbering',
    # 'extract_toc',
    'i18n_subsites',
    # 'disqus_static',
    # 'better_figures_and_images'
    ]
MARKDOWN = {'extensions': ['codehilite','extra','smarty', 'toc']}
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_SUBSITES = {
    'pt': {
        'SITENAME': 'Publicações acadêmicas',
        }
    }

# PLUGINS += ['subcategory']
# CATEGORIES_SAVE_AS = 'categories.html'
# CATEGORY_URL = 'category/{slug}.html'
# CATEGORY_SAVE_AS = 'category/{slug}.html'
# SUBCATEGORY_SAVE_AS = 'category/{savepath}/index.html'
# SUBCATEGORY_URL = 'category/{savepath}/'
# ARTICLE_URL = '{suburl}/{slug}.html'
# ARTICLE_SAVE_AS = '{subpath}/{slug}.html'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# SUBCATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

PLUGINS += ['render_math']
MATH_JAX = {'align': 'left',
            'indent': '2em',
            'responsive': True,
            'autoNumber': 'AMS'}

PLUGINS += ['summary']
SUMMARY_BEGIN_MARKER = '<!-- PELICAN_BEGIN_SUMMARY -->'
SUMMARY_END_MARKER = '<!-- PELICAN_END_SUMMARY -->'

PLUGINS += ['tag_cloud']
TAG_CLOUD_STEPS = 5
TAG_CLOUD_BADGE = True

# PLUGINS += ['pelican_comment_system']
# PELICAN_COMMENT_SYSTEM = True
# PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = ('author','email')
# PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE = 75

# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

TAGS_SAVE_AS = 'tag.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-79742963-2'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'

DISQUS_SITENAME = "publicacoes-academicas"
DISQUS_NO_ID = True
DISQUSURL = 'https://fhcflx.github.io/alt-pub'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
