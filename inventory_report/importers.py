from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
# import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> List[Product]:
        with open(self.path, "r") as json_file:
            file = json.load(json_file)

        product_list = [
            Product(
                id=line["id"],
                product_name=line["product_name"],
                company_name=line["company_name"],
                manufacturing_date=line["manufacturing_date"],
                expiration_date=line["expiration_date"],
                serial_number=line["serial_number"],
                storage_instructions=line["storage_instructions"],
            )
            for line in file
        ]

        return product_list


class CsvImporter(Importer):
    pass
    # def __init__(self, path: str) -> None:
    #     super().__init__(path)

    # def import_data(self) -> List[Product]:

    #     with open(self.path, "r") as csv_file:
    #         file = csv.DictReader(csv_file)

    #     product_list = [
    #         Product(
    #             id=line["id"],
    #             product_name=line["product_name"],
    #             company_name=line["company_name"],
    #             manufacturing_date=line["manufacturing_date"],
    #             expiration_date=line["expiration_date"],
    #             serial_number=line["serial_number"],
    #             storage_instructions=line["storage_instructions"],
    #         )
    #         for line in file
    #     ]

    #     return product_list


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
