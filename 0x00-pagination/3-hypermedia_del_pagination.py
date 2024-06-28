#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page of the dataset along with hypermedia information, resilient to deletions.

        Args:
        index (int): The current start index of the return page.
        page_size (int): The number of items per page.

        Returns:
        Dict[str, Any]: A dictionary containing the page information and hypermedia links.
        """
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset()), "index must be a valid integer within range"

        data = []
        next_index = index
        indexed_data = self.indexed_dataset()
        keys = sorted(indexed_data.keys())

        while len(data) < page_size and next_index < len(keys):
            key = keys[next_index]
            data.append(indexed_data[key])
            next_index += 1

        return {
                "index": index,
                "next_index": next_index if next_index < len(keys) else None,
                "page_size": len(data),
                "data": data
                }
