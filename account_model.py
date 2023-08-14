class Account:
    def __init__(self, acNum, transactions, balance):
        self.balance = balance
        self.transactions = transactions
        self.acNum = acNum
    def update_balance(self, amount, nature):
        if nature == 'credit':
            self.balance += amount
        elif nature == 'debit':
            self.balance -= amount

    def update_transaction(self, transaction):
        self.transactions.append(transaction)
