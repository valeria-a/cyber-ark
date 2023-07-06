from dataclasses import dataclass


@dataclass
class BankAccount:
    account_num: int
    owner_name: str
    _balance: float = 0

    def is_overdraft(self):
        return self.balance < 0

    @property
    def balance(self):
        return self._balance


if __name__ == '__main__':
    a1 = BankAccount(account_num=1, owner_name='moshe')
    a2 = BankAccount(account_num=2, owner_name='david')
    a3 = BankAccount(account_num=2, owner_name='david')
    a3.balance
    # print([a1, a2])
    # print(a2 == a3)
    # print((1,2,'apple',3) > (1,2,2))
