from flask import jsonify, make_response, Response


def make_resp(msg: str, data: str, code: int) -> Response:
    """
    This function returns valid HTTP response object

    :param:     msg: custom message for `message` response field
    :type:      str

    :param:     data: value of response data field
    :type:      str

    :param:     code: HTTP status code
    :type:      str

    :return:    valid HTTP response
    :rtype:     flask.Response
    """
    resp_body = dict(
        message=msg,
        data=data
    )
    return make_response(jsonify(resp_body), code)
