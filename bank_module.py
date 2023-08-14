from datetime import date


def show_balance(user, bank, account):
    account = bank.accounts[user]
    print(account.balance)



def withdraw_money(user, bank, amount):
    account = bank.accounts[user]

    if account.balance < amount:
        return None
    else:
        nature = 'debit'
        account.update_balance(amount, nature)

        id = len(account.transactions) + 1
        curr_date = date.today().strftime("%d/%m")
        desc = "Money withdrawn"

        transaction = {'id': id, 'date': curr_date, 'nature': nature, 'amt': amount, 'desc': desc}
        account.update_transaction(transaction)

        return transaction


def deposit_money(user, bank, amount):
    account = bank.accounts[user]
    nature = 'credit'
    account.update_balance(amount, nature)

    id = len(account.transactions) + 1
    curr_date = date.today().strftime("%d/%m")
    desc = "Money deposited"

    transaction = {'id': id, 'date': curr_date, 'nature': nature, 'amt': amount, 'desc': desc}
    account.update_transaction(transaction)

    return transaction


def transfer_money(bank, amount, from_user, to_user):
    if from_user in bank.accounts and to_user in bank.accounts:
        from_account = bank.accounts[from_user]
        to_account = bank.accounts[to_user]

        # sufficient balance for transfer?
        if from_account.balance >= amount:
            withdraw_trans = withdraw_money(from_user, bank, amount)
            deposit_trans = deposit_money(to_user, bank, amount)
            return withdraw_trans
        else:
            return None
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

