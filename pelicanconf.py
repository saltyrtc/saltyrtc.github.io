#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime
import os

base_dir = os.path.normpath(os.path.join(
    os.path.realpath(__file__),
    '..',
))

# Page information
SITEURL = ''
AUTHOR = 'SaltyRTC'
SITENAME = AUTHOR
#SITETITLE = AUTHOR
SITESUBTITLE = 'An end-to-end encrypted signalling protocol'
#SITEDESCRIPTION = '{} - {}'.format(SITENAME, SITESUBTITLE)
SITEICON = SITEURL + '/static/img/shaker.svg'

# Page settings
THEME = os.path.join(base_dir, 'themes', 'notmyidea')
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# Static paths & mapping
STATIC_PATHS = ('static',)
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon-64.png': {'path': 'favicon.ico'},
}

# Feed generation settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme specific settings
DISPLAY_CATEGORIES_ON_MENU = False  # Switch once first article in News has been created
DISPLAY_PAGES_ON_MENU = True
LINKS_WIDGET_NAME = 'Links'
SOCIAL_WIDGET_NAME = 'Social'

# Additional menu items
MENUITEMS = (
    ('Home', '/'),
)
SOCIAL = (
    ('Twitter', 'https://twitter.com/saltyrtc'),
    ('Github', 'https://github.com/saltyrtc/'),
)
LINKS = (
    ('Specification', 'https://github.com/saltyrtc/saltyrtc-meta/blob/master/Protocol.md'),
    ('WebRTC', 'https://webrtc.org/'),
    ('ORTC', 'https://ortc.org/'),
)

# Plugins
PLUGIN_PATHS = (
    os.path.join(base_dir, 'plugins',),
)
PLUGINS = ('sitemap',)

# Sitemap settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

