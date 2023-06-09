from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    MetaData,
)

from sqlalchemy.orm import registry
from domain.order import Order
from domain.person import Person


def create_tables_and_mappers(metadata: MetaData) -> None:
    person_table = Table(
        "person",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("age", Integer),
    )

    order_table = Table(
        "order",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("person_id", Integer, ForeignKey("person.id")),
        Column("order_date", String),
        Column("total_amount", Integer),
    )

    mapper_registry = registry()
    mapper_registry.map_imperatively(Person, person_table)
    mapper_registry.map_imperatively(Order, order_table)
