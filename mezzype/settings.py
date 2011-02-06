
import os, sys; sys.path.insert(0, os.path.join("..", "..", "..", "mezzanine"))
from mezzanine.project_template.settings import *

# Cartridge settings.
SHOP_SSL_ENABLED = False

# Mezzanine settings.
from django.utils.translation import ugettext_lazy as _
ADMIN_MENU_ORDER = (
    (_("Content"), ("pages.Page", "blog.BlogPost", "blog.Comment",
        (_("Media Library"), "fb_browse"),)),
    (_("Shop"), ("shop.Product", "shop.ProductOption", "shop.DiscountCode",
        "shop.Sale", "shop.Order")),
    (_("Site"), ("sites.Site", "redirects.Redirect", "conf.Setting")),
    (_("Users"), ("auth.User", "auth.Group",)),
)

THEME = ""

# Main Django settings.
DEBUG = False
DEV_SERVER = False
MANAGERS = ADMINS = ()
TIME_ZONE = ""
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
LANGUAGE_CODE = "en"
SITE_ID = 1
USE_I18N = False
SECRET_KEY = "9884fa44-f202-47c3-aa12-c8a610e7f62405c3771f-5ce4-404c-b1e1-2555810bf3c263784e0d-828f-448f-b967-fc1d8dec384e"
INTERNAL_IPS = ("127.0.0.1",)

# Databases.
DATABASES = {
    "default": {
        "ENGINE": "",
        "HOST": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "PORT": "",
    }
}

# Paths.
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
ADMIN_MEDIA_PREFIX = "/media/"
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME
MEDIA_URL = "/site_media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip("/"))
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

AUTHENTICATION_BACKENDS = (
    "userena.backends.UserenaAuthenticationBackend",
    "guardian.backends.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",
)

TEMPLATE_CONTEXT_PROCESSORS = tuple(TEMPLATE_CONTEXT_PROCESSORS) + (
    # ...
    "django.contrib.messages.context_processors.messages",
    # ...
    "cartridge.shop.context_processors.shop_globals",
)

MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES) + (
    # ...
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    # ...
    "userena.middleware.UserenaLocaleMiddleware",
    # ...
    "cartridge.shop.middleware.SSLRedirect",
)

# Apps.
INSTALLED_APPS = tuple(INSTALLED_APPS) + (
    # django
    "django.contrib.messages",
    # common
    "easy_thumbnails",
    "south",
    "emencia.django.countries",
    # userena
    "guardian",
    "userena",
    # shop
    "cartridge.shop",
    # bewype project
    "mezzype.app",
    )

# django emails
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 25
# EMAIL_HOST_USER = "florent.pigout@gmail.com"
# EMAIL_HOST_PASSWORD = ""

# Userena settings
LOGIN_REDIRECT_URL = "/accounts/%(username)s/"
LOGIN_URL = "/accounts/signin/"
LOGOUT_URL = "/accounts/signout/"
AUTH_PROFILE_MODULE = "app.Profile"

USERENA_DISABLE_PROFILE_LIST = False
USERENA_MUGSHOT_SIZE = 140

# Guardian
ANONYMOUS_USER_ID = -1

# Local settings.
try:
    from local_settings import *
except ImportError:
    pass

# Dynamic settings.
from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())
