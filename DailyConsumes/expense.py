class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description
    
    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }