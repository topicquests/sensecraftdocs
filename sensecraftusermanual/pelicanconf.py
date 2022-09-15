AUTHOR = '2022 TopicQuests Foundation, Conversence'
SITENAME = 'SenseCraft Manual'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.wikilinks': {
            'base_url': './',
            'end_url': '.html'
        }
    }
}
PAGES_SORT_ATTRIBUTE = 'menuorder'

DEFAULT_LANG = 'en'
PLUGIN_PATHS = ['/Users/jackpark/Documents/gitprojects6/pelican-plugins']
THEME = '/Users/jackpark/Documents/gitprojects6/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
PLUGINS = ['i18n_subsites']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('User Guide', 'usequests.html'),
)
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True