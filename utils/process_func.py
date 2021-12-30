def count_fibonacci(n: str) -> int:
    """
    This function calculates fibonacci number depends on value of n parameter

    :param:     n: value provided by user
    :type:      str

    :return:    Fibonacci number
    :rtype:     int
    """
    f1, f2 = 0, 1
    for _ in range(int(n)):
        f1, f2 = f2, f1 + f2

    return f1


def count_ackermann(m: str, n: str) -> int:
    """
    This function calculates ackermann number
    depends on values of n,m parameters

    :param:     m: value provided by user
    :type:      str

    :param:     n: value provided by user
    :type:      str

    :return:    Ackermann number
    :rtype:     int
    """
    if int(m) == 0:
        return int(n) + 1
    if int(m) > 0 and int(n) == 0:
        return count_ackermann(int(m) - 1, 1)
    if int(m) > 0 and int(n) > 0:
        return count_ackermann(int(m) - 1, count_ackermann(int(m), int(n) - 1))


def count_factorial(n: str) -> int:
    """
    This function calculates factorial number depends on value of n parameter

    :param:     n: value provided by user
    :type:      str

    :return:    Factorial number
    :rtype:     int
    """
    factorial = 1

    for i in range(2, int(n) + 1):
        factorial *= i

    return factorial


def count_func(**kw: dict) -> int:
    """
    This function returns calculated function
    which ws requested by func param defined by user

    :param: r**kw:
        See below

    :Keyword Arguments:
        :func   (``str``)
        function name which should be calculated

        :n   (``str``)
        value of n parameter

        :m   (``str``)
        value of m parameter

    :return:    Result of calculated function
    :rtype:     int
    """
    func_name = kw.get('func')
    n = kw.get('n')
    m = kw.get('m')

    if func_name == 'fibonacci':
        return count_fibonacci(n)
    elif func_name == 'ackermann':
        return count_ackermann(m, n)
    else:
        return count_factorial(n)
