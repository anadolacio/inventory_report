from inventory_report.product import Product


def test_create_product() -> None:
    data = {
        "id": "1",
        "product_name": "cadeira",
        "company_name": "Target Corporation",
        "manufacturing_date": "2021-02-18",
        "expiration_date": "2025-09-17",
        "serial_number": "CR25",
        "storage_instructions": "empilhas",
    }

    product = Product(**data)

    assert product.id == "1"
    assert product.company_name == "Target Corporation"
    assert product.product_name == "cadeira"
    assert product.manufacturing_date == "2021-02-18"
    assert product.expiration_date == "2025-09-17"
    assert product.serial_number == "CR25"
    assert product.storage_instructions == "empilhas"
