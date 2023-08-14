import datetime


def show_balance(user, account):
    account = bank.accounts[user]
    print(account.balance)


def withdraw_money(user, bank, amount):
    account = bank.accounts[user]
    nature = 'debit'
    account.update_balance(amount, nature)

    id = len(account.transactions) + 1
    date = datetime.today().strftime("%d/%m")
    desc = "Money withdrawn"

    transaction = {'id': id, 'date': date, 'nature': nature, 'amt': amount, 'desc': desc}
    account.update_transaction(transaction)

    return transaction


def deposit_money(user, bank, amount):
    account = bank.accounts[user]
    nature = 'credit'
    account.update_balance(amount, nature)

    id = len(account.transactions) + 1
    date = datetime.today().strftime("%d/%m")
    desc = "Money deposited"

    transaction = {'id': id, 'date': date, 'nature': nature, 'amt': amount, 'desc': desc}
    account.update_transaction(transaction)

    return transaction


def transfer_money(user, bank, amount, from_user, to_user):
    return transaction


def display_trans(user, bank):
    return transaction