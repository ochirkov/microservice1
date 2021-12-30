from flask import request, Response

from ..utils.response_body import make_resp
from ..utils.validate import validate
from ..utils.process_func import count_func
from ..utils.log_app import get_logged_app


flask_app = get_logged_app()
app = flask_app[0]
logger = flask_app[1]

@app.route('/', methods=['GET'])
def func() -> Response:
    """
    This is the Mathematical Web API
    Call this api passing a func name and get back its features

    :return: valid HTTP response
    :rtype: flask.Response
    """
    validation = validate(**request.args)
    if not validation[0]:
        logger.info(f"{request.args.get('func')}",
                    extra={'props': {"func": request.args.get('func'), "status": 400}})   # noqa: E501
        return make_resp(validation[1], "", 400)
    else:
        value = count_func(**request.args)
        logger.info(f"{request.args.get('func')}",
                    extra={'props': {"func": request.args.get('func'), "status": 200}})  # noqa: E501
        return make_resp(
            f"{request.args.get('func')} counted successfully",
            value,
            200
        )
