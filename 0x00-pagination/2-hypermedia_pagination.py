#!/usr/bin/env python3
"""
"""
import csv
from typing import List, Tuple, Dict, Union


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

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
        """
        Defines the information to be returned
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        s, e = self.index_range(page, page_size)
        return self.dataset()[s:e]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        This function takes two integer arguments and returns a tuple of
        size two containing a start index and an end index corresponding
        to the range of indexes to return in a list for those particular
        pagination parameters.
        """
        next_page = page * page_size
        return next_page - page_size, next_page

    def get_hyper(self, page: int,
                  page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        Hypermedia pagination represented as a dictionary of key value pairs.
        """
        data = self.get_page(page, page_size)
        totalRows = len(self.dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1
        if self.index_range(page, page_size)[1] >= totalRows:
            next_page = None
        total_pages = totalRows / page_size
        if total_pages % 1 != 0:
            total_pages += 1
        return {'page_size': len(data), 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': int(total_pages)}
