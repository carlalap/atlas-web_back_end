#!/usr/bin/env python3
"""task2. Simple pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """Function that takes two integer arguments page and page_size.
    The function should return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters."""
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
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
        """Retrieves a specified page of data from the dataset.
        It uses the index_range function to calculate
        the start and end indices for the desired page."""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        pages = []

        if start >= len(self.dataset()):

            return pages

        pages = self.dataset()

        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get_Hyper return a dictionary containing information
        about a specific page in the paginated dataset."""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_page = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1

        hyper_dict = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page * page_size <
            len(self.dataset()) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper_dict
