from adapters.in_memory_person_repository import InMemoryPersonRepository
from adapters.in_memory_order_repository import InMemoryOrderRepository
from adapters.in_memory_connection import InMemoryConnection
from use_cases.unit_of_work import UnitOfWork
from domain.person import Person
from domain.order import Order
from use_cases.create_person_and_order_use_case import (
    CreatePersonAndOrderUseCase)


connection = InMemoryConnection()
person_repository = InMemoryPersonRepository()
order_repository = InMemoryOrderRepository()

unit_of_work = UnitOfWork(connection, person_repository,
                          order_repository)
create_use_case = CreatePersonAndOrderUseCase(unit_of_work)

new_person = Person(name="John Doe", age=30)
new_order = Order(person_id=None, order_date="2023-04-03",
                  total_amount=100.0)

person, order = create_use_case.execute(new_person, new_order)
print(person)
print(order)
