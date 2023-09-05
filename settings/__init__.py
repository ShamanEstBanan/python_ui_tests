"""
Parent file with settings, can be override by local_settings
"""
IMPLICITLY_WAIT = 10
URL = 'https://www.w3schools.com/'

try:
    from .local_settings import *
except ImportError:
    pass
