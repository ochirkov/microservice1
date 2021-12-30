def validate_number(n: str, name: str) -> tuple:
    """
    This function validates value of parameters(m,n) which represent numbers

    :param:     n: value provided by user
    :type:      str

    :return:    tuple (bool, msg)
    :rtype:     tuple
    """
    if not n:
        return False, f"{name} param should be provided"

    try:
        int(n)
    except ValueError:
        return False, f"{name} should be number"

    if int(n) < 0:
        return False, f"{name} value should be greater or equal zero"
    else:
        return True, "Validation succeeded"


def validate_fibonacci(n: str) -> tuple:
    """
    This function validates Fibonacci input

    :param:     n: value provided by user
    :type:      str

    :return:    tuple (bool, msg)
    :rtype:     tuple
    """
    return validate_number(n, 'n')


def validate_ackermann(n: str, m: str) -> tuple:
    """
    This function validates Ackermann input

    :param:     n: value provided by user
    :type:      str

    :return:    tuple (bool, msg)
    :rtype:     tuple
    """
    validated_n = validate_number(n, 'n')
    if not validated_n[0]:
        return validated_n

    return validate_number(m, 'm')


def validate_factorial(n: str) -> tuple:
    """
    This function validates Factorial input

    :param:     n: value provided by user
    :type:      str

    :return:    tuple (bool, msg)
    :rtype:     tuple
    """
    return validate_number(n, 'n')


def validate_func(func: str) -> tuple:
    """
    This function validates func parameter

    :param:     func: value provided by user
    :type:      str

    :return:    tuple (bool, msg)
    :rtype:     tuple
    """
    functions = ('fibonacci', 'ackermann', 'factorial')
    if func not in functions:
        return False, f"func param should be one of {functions}"
    else:
        return True, ""


def validate(**kw: dict) -> tuple:
    """
    This function returns result of parameters validation
    which is a tuple with next format:

    (bool, msg):
        bool - result of validation
        msg - custom message for HTTP response

    :param: r**kw:
        See below

    :Keyword Arguments:
        :func   (``str``)
        function name which should be calculated

        :n   (``str``)
        value of n parameter

        :m   (``str``)
        value of m parameter

    :return:    Result of validated parameters
    :rtype:     tuple
    """
    func_name = kw.get('func', None)
    n = kw.get('n', None)
    m = kw.get('m', None)

    func_validation = validate_func(func_name)
    if not func_validation[0]:
        return func_validation

    funcs = {
        'fibonacci': validate_fibonacci(n),
        'ackermann': validate_ackermann(n, m),
        'factorial': validate_factorial(n)
    }

    return funcs[func_name]
