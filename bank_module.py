import datetime

def show_balance(account):
    pass
def withdraw_money(account, amount):
    pass


def deposit_money(account, amount):
    nature = 'credit'
    account.update_balance(amount, nature)
    id = len(account.transactions)+1
    date = datetime.today.strftime("%d/%m")
    desc = "Money deposited"
    transaction = {'id':id, 'date':date, 'nature':nature, 'desc': desc} #{id:, date:, amt:, nature:, desc:}
    account.update_transanction(transaction)

def transfer_money(amount, from_acc, to_acc):
    from_acc.update_balance(amount, 'debit')
    to_acc.update_balance(amount, 'credit')

def display_trans(account):
    trans = account.transactions[-10:]
    for tran in trans:
        for k,v in tran.items():
            print(f"{k}: {v}\n")
