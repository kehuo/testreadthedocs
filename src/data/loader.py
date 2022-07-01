# !/usr/bin/env python3
# -*- coding:utf-8 -*-


class Loader(object):
    """
    A data loader

    Args:
        dtype(str): target data type to load.

    Attributes:
        _dtype(str): target data type to load.
    """
    def __init__(self, dtype: str):
        self._dtype = dtype

    def load(self, path: str) -> bool:
        """
        Loads data and return the path.

        Args:
            path(str): path to load data.

        Returns:
            bool: if loads succeed.
        """
        return True
