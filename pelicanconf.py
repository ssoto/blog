#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from os.path import expanduser

AUTHOR = u'Sergio Soto'
SITENAME = u'Technical box'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_FOLDER_AS_CATEGORY = True

THEME = expanduser('./themes/pelican-clean')
DISPLAY_PAGES_ON_MENU = True
GITHUB_URL = 'http://github.com/ssoto'
TWITTER_URL = 'http://twitter.com/sototan'
FACEBOOK_URL = 'https://www.facebook.com/ser.soton'
LINKEDIN = 'https://www.linkedin.com/in/sergiosotonunez'

COLOR_SCHEME_CSS = 'monokai.css'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
