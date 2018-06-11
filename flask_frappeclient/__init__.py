# -*- coding: utf-8 -*-
"""
    __init__.py
    :copyright: (c) 2018 by Joe Paul.
    :license: see LICENSE for details.
"""
from frappe_client import FrappeRequest


__all__ = ('FlaskFrappe', )
__version__ = '0.1.0'


class FlaskFrappe(object):
    """
        Flask extension for frappe api
        app = Flask(__name__)
        frappeclient = FlaskFrappe(app)
    """

    def __init__(self, app=None):
        self._client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the frappe client
        :param app: Flask app instance
        """
        self._client = FrappeRequest(
            url=app.config.get('FRAPPE_URL'),
            username=app.config.get('FRAPPE_USERNAME'),
            password=app.config.get('FRAPPE_PASSWORD')
        )

    def __getattr__(self, name):
        """Proxy methods to the private held object
        """
        return getattr(self._client, name)
