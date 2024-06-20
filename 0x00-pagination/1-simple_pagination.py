#!/usr/bin/env python3
"""
This module provides a function to calculate the start and end indices
for paginated results.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and end index (exclusive) for the items on the specified page.
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            Must be a positive integer.
            page_size (int): The number of items per page.
            Must be a positive integer.

        Returns:
            List[List[str]]: The list of rows corresponding to
            the specified page,
            or an empty list if the input is out of range.
        """
        assert isinstance(page, int) and page > 0, "page must be a"
        "positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size"
        "must be a positive integer"

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]
