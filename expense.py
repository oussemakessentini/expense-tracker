class Expense:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def to_list(self):
        return [
            self.description,
            self.amount,
            self.category,
            self.date
        ]