# ===========================
# Basic Site Information
# ===========================
AUTHOR = 'Aron Green'
SITENAME = 'Aron Green (dot) com'

# ===========================
# Localization and Timezone
# ===========================
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# ===========================
# Content and Output Settings
# ===========================
PATH = "content"
DEFAULT_PAGINATION = 10
DIRECT_TEMPLATES = ['index']

# ===========================
# URL and Site Settings
# ===========================
SITEURL = ""
RELATIVE_URLS = True  # Ensure relative URLs for development

# ===========================
# Theme and Appearance
# ===========================
THEME = 'theme/m.css/pelican-theme'
THEME_STATIC_DIR = 'static'

# ===========================
# Static Files and CSS
# ===========================
STATIC_PATHS = [
    'theme/m.css/pelican-theme/static',
    'static'
]

M_CSS_FILES = [
    'https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i|Source+Code+Pro:400,400i,600',
    '/static/m-light.css',  # Use '/static/m-dark.css' for dark mode if preferred
    '/static/m-theme-arongreen.css'  # Custom overrides
]

M_THEME_COLOR = '#006400'  # Dark green for your color palette

# ===========================
# Plugins
# ===========================
PLUGIN_PATHS = ['theme/m.css/plugins']
PLUGINS = ['m.htmlsanity', 'm.components', 'm.images', 'm.code', 'm.math']

# ===========================
# Feed Settings (disabled for development)
# ===========================
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ===========================
# Blogroll (external links)
# ===========================
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# ===========================
# Social Widget
# ===========================
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
