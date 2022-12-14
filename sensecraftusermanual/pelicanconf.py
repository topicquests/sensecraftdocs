import os

AUTHOR = '2022 TopicQuests Foundation, Conversence'
SITENAME = 'SenseCraft Manual'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

from markdown.extensions.tables import TableExtension

MARKDOWN = {
    'extensions': ['wikilinks', 'attr_list', TableExtension()],
    'extension_configs': {
        'markdown.extensions.wikilinks': {
            'base_url': './',
            'end_url': '.html'
        },
        'markdown.extensions.extra': {},
    }
}
PAGES_SORT_ATTRIBUTE = 'menuorder'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = [os.environ['PELICAN_PLUGINS_PATH']]
THEME = os.environ['PELICAN_THEMES_PATH'] + '/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
PLUGINS = ['i18n_subsites']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['css']
CUSTOM_CSS = SITEURL + '/css/extra.css'
DISPLAY_BREADCRUMBS = True
DISPLAY_PAGES_ON_MENU=False

# Blogroll
LINKS = (('User Guide', 'usequests.html'), ('Jonathan', 'jonathan/sensecraft.html'),
)
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
