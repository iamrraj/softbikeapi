MEDIA_ROOT = '../media/'
STATIC_ROOT = '../static/'


try:
    from .localsettings import *
except ImportError:
    pass
