#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Page settings
SITEURL = 'http://saltyrtc.org'
RELATIVE_URLS = False

# Add CNAME
EXTRA_PATH_METADATA['static/CNAME'] = {'path': 'CNAME'}

# Feed generation settings
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Cleanup
DELETE_OUTPUT_DIRECTORY = True

# Disqus
#DISQUS_SITENAME = ''  # TODO

