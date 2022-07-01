# !/usr/bin/env python3
# -*- coding:utf-8 -*-


class Service(object):
    """
    A test python class, test rst syntax :class:`pandas.TimeStamp`.

    Args:
        name(str): This is name, This is name, This is name, This is name, This is name, This is name,
            This is name, ok reaches new line.
        age(int): This is age, This is age, This is age, This is age, This is age, This is age, This is age,
            This is age, ok reaches new line.


    Attributes:
        _name(str): This is name, This is name, This is name, This is name, This is name, This is name,
            This is name, ok reaches new line.
        _age(int): This is age, This is age, This is age, This is age, This is age, This is age, This is age,
            This is age, ok reaches new line.
    """
    def __init__(self, name: str, age: str, job: str):
        self._name = name
        self._age = age

    def run(self, host: str, port: int, timeout: bool = False) -> bool:
        """
        Run the application on the given host.

        Args:
            host(str): the host to run the app.
            port(int): the port to listen to the request.
            timeout(bool, optional): if supports timeout, default is not supported.

        Returns:
            bool: if runs succeed.

        Examples:
            .. code-block:: python

                # This is to test if multiple code blocks are supported in a single docstring.
                a = 1
                print("this is the first code block")

            .. code-block:: python

                # This is the second code block
                a = 2
                print("this is the second code block")
        """
        return True
