from bank_module import show_balance, withdraw_money, deposit_money, transfer_money, display_trans
from bank_model import Bank
from account_model import Account

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

def main():
    end = False
    user = input("What is your name?").strip()
    bank = Bank(user_accounts)

    while not end:
        service = int(input('''Choose a service!\n
                        1: Deposit\n
                        2: Withdraw\n
                        3: Transfer\n
                        4: Show Balance\n
                        5: Display Transactions\n
                        6: Quit\n'''))
        if service == 1:
            amount = float(input("Please input the deposit amount: "))
            transaction = deposit_money(user, bank, amount)
            print(f"Transaction ID: {transaction['id']}")
            print(f"Date: {transaction['date']}")
            print(f"Amount: {transaction['amt']}")
            print(f"Nature: {transaction['nature']}")
            print(f"Description: {transaction['desc']}")
            print("------------------------")
            continue
        elif service == 2:
            amount = float(input("Please input the withdraw amount: "))
            transaction = withdraw_money(user, bank, amount)
            if transaction:
                print(f"Transaction ID: {transaction['id']}")
                print(f"Date: {transaction['date']}")
                print(f"Amount: {transaction['amt']}")
                print(f"Nature: {transaction['nature']}")
                print(f"Description: {transaction['desc']}")
                print("------------------------")
            else:
                print("Not enough balance!")
            continue
        elif service == 3:
            from_user = user
            to_user = input("Who is the recipient?").strip()
            amount = float(input("What is the transfer amount?"))
            withdraw_transaction = transfer_money(bank, amount, from_user, to_user)
            if withdraw_transaction:
                print(f"Transaction ID: {withdraw_transaction['id']}")
                print(f"Date: {withdraw_transaction['date']}")
                print(f"Amount: {withdraw_transaction['amt']}")
                print(f"Nature: {withdraw_transaction['nature']}")
                print(f"Description: {withdraw_transaction['desc']}")
                print("------------------------")
            else:
                print(f"Insufficient balance in {from_user}'s account for transfer or {to_user}'s account doesn't exist")
            continue
        elif service == 4:
            show_balance(user, bank)
            continue
        elif service == 5:
            display_trans(user, bank)
            continue
        elif service == 6:
            end = True
            print("Quit")
        else:
            print("Please enter a valid choice: ")
            continue

main()