from inventory_report.product import Product
import pytest


@pytest.mark.parametrize(
    "data, expected_result",
    [
        (
            {
                "id": "1",
                "product_name": "cadeira",
                "company_name": "Target Corporation",
                "manufacturing_date": "2021-02-18",
                "expiration_date": "2025-09-17",
                "serial_number": "CR25",
                "storage_instructions": "empilhas",
            },
            """The product 1 - cadeira with serial number CR25 manufactured on 2021-02-18 by the company Target Corporation valid until 2025-09-17 must be stored according to the following instructions: empilhas.""",
        ),
    ],
)
def test_product_report(data, expected_result) -> None:
    # raise NotImplementedError
    product = Product(**data)

    assert str(product) == str(expected_result)
