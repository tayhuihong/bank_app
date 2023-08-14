import bank_module
from bank_model import Account
from account_model import Bank
import datetime
import random

## Initiate 10 Account classes
accounts = [
    {'Amy': Account([], 500)},
    {'Ben': Account([], 500)},
    {'Charlie': Account([], 500)},
    {'Dan': Account([], 500)},
    {'Emily': Account([], 500)},
    {'Frans': Account([], 500)},
    {'Gufran': Account([], 500)},
    {'Hendy': Account([], 500)},
    {'Zoe': Account([], 500)},
    {'Jill': Account([], 500)},
]

## Initiate Bank class with accounts
bank = Bank(accounts)


