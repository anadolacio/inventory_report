from inventory_report.product import Product
from typing import List, Union


class Inventory:
    def __init__(self, data: Union[List[Product], None] = None):
        if data is None:
            data = []
        self._data = data

    def add_data(self, data: List[Product]) -> None:
        self._data.extend(data)

    @property
    def data(self) -> List[Product]:
        return self._data
