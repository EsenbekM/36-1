from pathlib import Path


# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key - Django will use this to encrypt and sign things
SECRET_KEY = 'django-insecure-jps1*!j$q%&w5nki3#o0+)4f96z@1qv2^nsb*c6f)7v3i$y)es'

# Debug mode - True means we're in development
DEBUG = True

# Allowed hosts - Django will only serve requests from these hosts
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'jazzmin', # Jazzmin admin theme
    
    # installed apps
    'django.contrib.admin', # Django's admin site
    'django.contrib.auth', # Django's authentication framework
    'django.contrib.contenttypes', # Django's content types framework
    'django.contrib.sessions', # Django's session framework
    'django.contrib.messages', # Django's messaging framework (for errors, etc.)
    'django.contrib.staticfiles', # Django's static file framework

    # my apps
    'post',
    'user',

    # third-party apps
]

# Middleware - code that runs before and after views are called
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware', # Session middleware
    'django.middleware.common.CommonMiddleware', # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware', # CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware', # Message middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking middleware
]

# root URL configuration - tells Django where to find the root URL configuration module
ROOT_URLCONF = 'blog.urls'

# Template configuration - tells Django how to load templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates", # Tells Django to look for templates in the templates/ directory
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application - tells Django where your WSGI application is
WSGI_APPLICATION = 'blog.wsgi.application'


# Database - tells Django how to connect to your database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Tells Django which database engine to use
        'NAME': BASE_DIR / 'db.sqlite3', # Tells Django the name of your database file
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/' # URL, по которому будут доступны статические файлы
STATICFILES_DIRS = [ # папки, в которых Django будет искать статические файлы
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles" # папка, в которую Django будет собирать статические файлы

MEDIA_URL = '/media/' # URL, по которому будут доступны медиа файлы
MEDIA_ROOT = BASE_DIR / "media" # папка, в которую Django будет сохранять медиа файлы

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title": "Blog 36-1",
    "site_header": "Blog",
    "site_brand": "Blog",
    "site_logo": "catMeme.jpg",
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the library",

    # Copyright on the footer
    "copyright": "Acme Library Ltd",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "ДОМ",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

# JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text": False,
#     "footer_small_text": False,
#     "body_small_text": False,
#     "brand_small_text": False,
#     "brand_colour": False,
#     "accent": "accent-primary",
#     "navbar": "navbar-dark",
#     "no_navbar_border": False,
#     "navbar_fixed": False,
#     "layout_boxed": False,
#     "footer_fixed": False,
#     "sidebar_fixed": False,
#     "sidebar": "sidebar-dark-primary",
#     "sidebar_nav_small_text": False,
#     "sidebar_disable_expand": False,
#     "sidebar_nav_child_indent": False,
#     "sidebar_nav_compact_style": False,
#     "sidebar_nav_legacy_style": False,
#     "sidebar_nav_flat_style": False,
#     "theme": "darkly",
#     "dark_mode_theme": None,
#     "button_classes": {
#         "primary": "btn-primary",
#         "secondary": "btn-secondary",
#         "info": "btn-info",
#         "warning": "btn-warning",
#         "danger": "btn-danger",
#         "success": "btn-success"
#     }
# }

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="esenbekm03@gmail.com"
EMAIL_HOST_PASSWORD=""
EMAIL_PORT=587
EMAIL_USE_TLS=True
