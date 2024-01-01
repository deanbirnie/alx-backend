#!/usr/bin/env python3
"""
This module contains a function that defines the start and end indexes for
the range of indexes to return.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function takes two integer arguments and returns a tuple of size two
    containing a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    """
    next_page = page * page_size
    return next_page - page_size, next_page
