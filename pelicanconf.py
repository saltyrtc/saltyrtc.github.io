#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SaltyRTC'
SITENAME = 'SaltyRTC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'themes/notmyidea'

STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon-64.png': {'path': 'favicon.ico'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Additional menu items
MENUITEMS = (('Home', '/'),)

# Blogroll
LINKS = (
    ('Specification', 'https://github.com/saltyrtc/saltyrtc-meta/blob/master/Protocol.md'),
    ('WebRTC', 'https://webrtc.org/'),
    ('ORTC', 'https://ortc.org/'),
)
LINKS_WIDGET_NAME = 'Links'

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/saltyrtc'),
    ('Github', 'https://github.com/saltyrtc/'),
)
SOCIAL_WIDGET_NAME = 'Social'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
