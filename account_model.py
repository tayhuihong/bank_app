class Account:
    def __init__(self, transactions, balance):
        self.balance = balance
        self.transactions = transactions #{id:, date:, amt:, nature:, desc:}
    def update_balance(self, amount, nature):
        if nature == 'credit':
            self.balance += amount
        elif nature == 'debit':
            self.balance -= amount
    def update_transaction(self, transaction):
        self.transactions.append(transaction)
