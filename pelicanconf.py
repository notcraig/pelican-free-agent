#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Free Agent'
SITENAME = 'Free Agent'
SITETITLE = 'Free Agent'
SITESUBTITLE = "A bootstrap one page theme for Pelican"
SITEURL = 'http://localhost:8000'


THEME = 'pelican-free-agent'
THEME_STATIC_DIR = 'theme'
PATH = 'content'
#STATIC_PATHS = [ 'mail','js', 'css', 'fonts']
#add images back in above
# EXTRA_PATH_METADATA = {
#     'static/images/portfolio': {'path': 'images/portfolio'},
#     }
TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'

SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']
DELETE_OUTPUT_DIRECTORY = True
# Top Menu Links
NAVLINKS = (
	#('#page-top', 'Home'),
	('#services','Services'),
	('#portfolio', 'Portfolio'),
	('#about', 'About'),
	('#contact', 'Contact')
)

# Portfolio Name
PORTFOLIO = 'Portfolio'



#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],

	['Message', 'textarea', 'message', 'Please enter a message.']
)
