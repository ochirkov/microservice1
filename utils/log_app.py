import logging
import sys

from flask import Flask
import json_logging


def get_logged_app() -> Flask:
    """
    This function returns Flask app object wrapped into json_logging

    :return: Flask app object
    :rtype: flask.Flask
    """
    app = Flask(__name__)
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_flask(enable_json=True)
    json_logging.init_request_instrument(app)

    logger = logging.getLogger("klarna-logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    return app, logger
