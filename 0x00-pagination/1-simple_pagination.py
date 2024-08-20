#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """return start and end index for pagination parameters
        Args:
            page: page number
            page_size: size of data per page
        Returns:
            tuple of start index and end index correspondin to range of indices
        """
        return ((page - 1) * page_size, page * page_size)

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get items for a given range
        """
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]
