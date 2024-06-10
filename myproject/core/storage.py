import os

from django.conf import settings
from django.core.files.storage import Storage


class MockStorage(Storage):

    def __init__(self, option=None):
        pass

    def _save(self, name, content):
        return name

    def _open(self, name, mode='rb'):
        return name

    def exists(self, name):
        path = os.path.join(settings.BASE_DIR, name)
        if os.path.exists(path):
            return True
        return False
