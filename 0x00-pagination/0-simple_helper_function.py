#!/usr/bin/env python3
"""a simple helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start and end index for pagination parameters
    Args:
        page: page number
        page_size: size of data per page
    Returns:
        tuple of start index and end index correspondin to range of indices
    """
    return ((page - 1) * page_size, page * page_size)
