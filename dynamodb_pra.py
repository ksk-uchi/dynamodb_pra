from __future__ import annotations
from typing import Generator
from contextlib import contextmanager

from models.customer import CustomerModel


@contextmanager
def my_dynamo() -> Generator:
    if not CustomerModel.exists():
        CustomerModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    yield
    CustomerModel.delete_table()


def main() -> None:
    import ipdb;ipdb.set_trace()
    ...


if __name__ == "__main__":
    with my_dynamo():
        main()
