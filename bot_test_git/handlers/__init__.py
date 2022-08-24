#from handlers import client
#from handlers import admin
#from handlers import other

from .admin import dp
from .client import dp

__all__ = ['dp']