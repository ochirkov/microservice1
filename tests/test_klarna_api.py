#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Unittest for klarna-api"""
from nose2.tools import params
import unittest
from flask import jsonify, make_response, Flask

# custom import
from utils.validate import validate_number, validate_fibonacci, \
    validate_ackermann, validate_factorial, validate_func, validate
from utils.process_func import count_fibonacci, count_ackermann, \
    count_factorial, count_func
from utils.response_body import make_resp


class TestKlarnaApi(unittest.TestCase):
    def setUp(self) -> None:
        """Run before every test method"""
        pass

    def tearDown(self) -> None:
        """Run after every test method"""
        pass

    @params(
        ('1', 'n', (True, 'Validation succeeded')),
        ('222', 'm', (True, 'Validation succeeded')),
        ('h', 'n', (False, 'n should be number')),
        ('-3', 'm', (False, 'm value should be greater or equal zero'))
    )
    def test_validate_number(
            self,
            number: str,
            msg: str,
            expectation: tuple
    ) -> None:
        """
        Test number validation passed into API as a parameter
        """
        result = validate_number(number, msg)
        self.assertEqual(result, expectation)

    @params(
        ('1', (True, 'Validation succeeded')),
        ('222', (True, 'Validation succeeded')),
        ('hgf', (False, 'n should be number')),
        ('-3', (False, 'n value should be greater or equal zero'))
    )
    def test_validate_fibonacci(self, n: str, expectation: tuple) -> None:
        """
        Test fibonacci related params validation
        """
        result = validate_fibonacci(n)
        self.assertEqual(result, expectation)

    @params(
        ('1', '1', (True, 'Validation succeeded')),
        ('0', '1', (True, 'Validation succeeded')),
        ('hgf', '1', (False, 'm should be number')),
        ('2', 'hghg', (False, 'n should be number')),
        ('-3', '2', (False, 'm value should be greater or equal zero'))
    )
    def test_validate_ackermann(
            self,
            m: str,
            n: str,
            expectation: tuple
    ) -> None:
        """
        Test fibonacci related params validation
        """
        result = validate_ackermann(n, m)
        self.assertEqual(result, expectation)

    @params(
        ('1', (True, 'Validation succeeded')),
        ('222', (True, 'Validation succeeded')),
        ('hgf', (False, 'n should be number')),
        ('-3', (False, 'n value should be greater or equal zero'))
    )
    def test_validate_factorial(self, n: str, expectation: tuple) -> None:
        """
        Test factorial related params validation
        """
        result = validate_factorial(n)
        self.assertEqual(result, expectation)

    @params(
        ('fibonacci', (True, '')),
        ('factorial', (True, '')),
        ('ackermann', (True, '')),
        ('something', (False, "func param should be one of ('fibonacci', 'ackermann', 'factorial')"))  # noqa: E501
    )
    def test_validate_func(self, func: str, expectation: tuple) -> None:
        """
        Test validation of func parameter value
        """
        result = validate_func(func)
        self.assertEqual(result, expectation)

    @params(
        (
            (True, 'Validation succeeded'),
            {'func': 'fibonacci', 'n': '1'}
        ),
        (
            (False, 'n value should be greater or equal zero'),
            {'func': 'fibonacci', 'n': '-1'}
        ),
        (
            (True, 'Validation succeeded'),
            {'func': 'factorial', 'n': '5'}
        ),
        (
            (True, 'Validation succeeded'),
            {'func': 'ackermann', 'n': '1', 'm': '1'}
        ),
        (
            (False, "func param should be one of ('fibonacci', 'ackermann', 'factorial')"),  # noqa: E501
            {'func': 'something', 'n': '1', 'm': '1'}
        ),
    )
    def test_validate(self, expectation: tuple, kw: dict) -> None:
        """
        Test validate func
        """
        result = validate(**kw)
        self.assertEqual(result, expectation)

    @params(
        ('1', 1),
        ('2', 1),
        ('5', 5),
        ('0', 0)
    )
    def test_count_fibonacci(self, n: str, expectation: tuple) -> None:
        """
        Test fibonacci calculation
        """
        result = count_fibonacci(n)
        self.assertEqual(result, expectation)

    @params(
        ('1', 1),
        ('2', 2),
        ('5', 120),
        ('0', 1)
    )
    def test_count_factorial(self, n: str, expectation: int) -> None:
        """
        Test factorial calculation
        """
        result = count_factorial(n)
        self.assertEqual(result, expectation)

    @params(
        ('1', '1',  3),
        ('0', '0',  1),
        ('0', '1', 2)
    )
    def test_count_ackermann(self, m: str, n: str, expectation: int) -> None:
        """
        Test ackermann calculation
        """
        result = count_ackermann(m, n)
        self.assertEqual(result, expectation)

    @params(
        (
            1,
            {'func': 'fibonacci', 'n': '1'}
        ),
        (
            1,
            {'func': 'fibonacci', 'n': '2'}
        ),
        (
            120,
            {'func': 'factorial', 'n': '5'}
        ),
        (
            3,
            {'func': 'ackermann', 'n': '1', 'm': '1'}
        )
    )
    def test_count_func(self, expectation: int, kw: dict) -> None:
        """
        Test ackermann calculation
        """
        result = count_func(**kw)
        self.assertEqual(result, expectation)

    def test_make_resp(self) -> None:
        """
        Test make_resp returns valid Flask response obj
        """
        with Flask(__name__).app_context():
            result = make_resp('test message', 'test data', 400)
            expectation = make_response(jsonify({'message': 'test message', 'data': 'test data'}), 400)  # noqa: E501
            self.assertEqual(result.status_code, expectation.status_code)
            self.assertEqual(result.data, expectation.data)

            result = make_resp('test valid message', 'test valid data', 200)
            expectation = make_response(jsonify({'message': 'test valid message', 'data': 'test valid data'}), 200)  # noqa: E501
            self.assertEqual(result.status_code, expectation.status_code)
            self.assertEqual(result.data, expectation.data)


if __name__ == '__main__':
    unittest.main()
