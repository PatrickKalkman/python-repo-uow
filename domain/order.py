class Order:
    def __init__(self, person_id: int, order_date: str, total_amount: float,
                 id: int = None):
        self.id = id
        self.person_id = person_id
        self.order_date = order_date
        self.total_amount = total_amount

    def __str__(self):
        return f'Order(id={self.id}, person_id={self.person_id}, order_date={self.order_date}, total_amount={self.total_amount})'
