from datetime import datetime

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

        
class Bank:
    def __init__(self, accounts):
        self.accounts = accounts


user_accounts = {
    "John Doe": Account("1234567890", [], 0),
    "Jane Smith": Account("9876543210", [], 0),
    "Michael Johnson": Account("5678901234", [], 0),
    "Emily Davis": Account("4321098765", [], 0),
    "Robert Wilson": Account("7890123456", [], 0),
    "Sarah Thompson": Account("2109876543", [], 0),
    "David Anderson": Account("6543210987", [], 0),
    "Jennifer Brown": Account("3456789012", [], 0),
    "Daniel Lee": Account("9012345678", [], 0),
    "Olivia Taylor": Account("4567890123", [], 0)
}


def show_balance(user, bank):
    #if user in bank.accounts:
    account = bank.accounts[user]
    print(account.balance)
    #else:
        #print(f"No account found for user: {user}")


def withdraw_money(user, bank, amount):
    account = bank.accounts[user]
    nature = 'debit'
    account.update_balance(amount, nature)

    id = len(account.transactions) + 1
    date = datetime.today().strftime("%d/%m")
    desc = "Money withdrawn"

    transaction = {'id': id, 'date': date, 'nature': nature, 'amt': amount, 'desc': desc}
    account.update_transaction(transaction)
    
    print(f"Transaction ID: {transaction['id']}")
    print(f"Date: {transaction['date']}")
    print(f"Nature: {transaction['nature']}")
    print(f"Amount: {transaction['amt']}")
    print(f"Description: {transaction['desc']}")
    print("------------------------")


def deposit_money(user, bank, amount):
    account = bank.accounts[user]
    nature = 'credit'
    account.update_balance(amount, nature)
    
    id = len(account.transactions) + 1
    date = datetime.today().strftime("%d/%m")
    desc = "Money deposited"
    
    transaction = {'id': id, 'date': date, 'nature': nature, 'amt': amount, 'desc': desc}
    account.update_transaction(transaction)
    
    print(f"Transaction ID: {transaction['id']}")
    print(f"Date: {transaction['date']}")
    print(f"Nature: {transaction['nature']}")
    print(f"Amount: {transaction['amt']}")
    print(f"Description: {transaction['desc']}")
    print("------------------------")
    
               

def transfer_money(user, bank, amount, from_user, to_user):
    if from_user in bank.accounts and to_user in bank.accounts:
        from_account = bank.accounts[from_user]
        to_account = bank.accounts[to_user]

        # sufficient balance for transfer?
        if from_account.balance >= amount:
            
            # Update balances 
            from_account.update_balance(amount, 'debit')
            to_account.update_balance(amount, 'credit')

            from_id = len(from_account.transactions) + 1
            from_date = datetime.today().strftime("%d/%m")
            from_desc = f"Transfer to {to_user}"
            from_transaction = {'id': from_id, 'date': from_date, 'amt': amount, 'nature': 'debit', 'desc': from_desc}
            from_account.update_transaction(from_transaction)

            
            to_id = len(to_account.transactions) + 1
            to_date = datetime.today().strftime("%d/%m")
            to_desc = f"Transfer from {from_user}"
            to_transaction = {'id': to_id, 'date': to_date, 'amt': amount, 'nature': 'credit', 'desc': to_desc}
            to_account.update_transaction(to_transaction)

            return True
        else:
            print(f"Insufficient balance in {from_user}'s account for transfer.")
            return False
    else:
        print("One or both users do not have an account.")
        return False


def display_trans(user, bank):
    if user in bank.accounts:
        account = bank.accounts[user]
        transactions = account.transactions
        if len(transactions) > 0:
            for transaction in transactions:
                print(f"Transaction ID: {transaction['id']}")
                print(f"Date: {transaction['date']}")
                print(f"Amount: {transaction['amt']}")
                print(f"Nature: {transaction['nature']}")
                print(f"Description: {transaction['desc']}")
                print("------------------------")
        else:
            print("No transactions found for this account.")
    else:
        print(f"No account found for user: {user}")

        


def main():
    end = False
    user = input("What is your name?").strip()
    bank = Bank(user_accounts)
    
    while end== False:
        service = int(input('''Choose a service!\n
                        1: Deposit\n
                        2: Withdraw\n
                        3: Transfer\n
                        4: Show Balance\n
                        5: Display Transactions\n
                        6: Quit'''))
        if service == 1:
            amount = float(input("Please input the deposit amount: "))
            deposit_money(user, bank, amount)
        elif service == 2:
            amount = float(input("Please input the withdraw amount: "))
            withdraw_money(user, bank, amount)
        elif service == 3:
            from_user = user
            to_user = input("Who is the recipient?").strip()
            amount = float(input("What is the transer amount?"))
            transfer_money(user, bank, amount, from_user, to_user)
        elif service == 4:
            show_balance(user, bank)
        elif service == 5:
            display_trans(user, bank)
        elif service == 6:
            end = True
            print("Quit")
            
        
main()
