"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay_type, base_pay, hours_worked=None, hourly_rate=None, contracts=None, commission_rate=None, bonus=None):
        self.name = name
        self.pay_type = pay_type
        self.base_pay = base_pay
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.contracts = contracts
        self.commission_rate = commission_rate
        self.bonus = bonus

    def get_pay(self):
        if self.pay_type == 'monthly':
            return self.base_pay
        elif self.pay_type == 'hourly':
            return self.hours_worked * self.hourly_rate if self.hours_worked is not None and self.hourly_rate is not None else 0
        elif self.pay_type == 'contract':
            contract_pay = self.hours_worked * self.hourly_rate if self.hours_worked is not None and self.hourly_rate is not None else 0
            commission_pay = self.contracts * self.commission_rate if self.contracts is not None and self.commission_rate is not None else 0
            bonus_pay = self.bonus if self.bonus is not None else 0
            return contract_pay + commission_pay + bonus_pay

    def __str__(self):
        if self.pay_type == 'monthly':
            return f'{self.name} works on a monthly salary of {self.base_pay}.\nTheir total pay is {self.get_pay()}.'
        elif self.pay_type == 'hourly':
            return f'{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour.\nTheir total pay is {self.get_pay()}.'
        elif self.pay_type == 'contract':
            contract_pay = self.hours_worked * self.hourly_rate if self.hours_worked is not None and self.hourly_rate is not None else 0
            commission_pay = self.contracts * self.commission_rate if self.contracts is not None and self.commission_rate is not None else 0
            bonus_pay = self.bonus if self.bonus is not None else 0
            total_pay = contract_pay + commission_pay + bonus_pay
            return f'{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.contracts} contract(s) at {self.commission_rate}/contract.\nTheir total pay is {total_pay}.'

# Test cases
# (Assuming the correct test cases are provided, the following instances should pass the tests)

billie = Employee("Billie", "monthly", 4000)
charlie = Employee("Charlie", "hourly", None, 100, 25)
renee = Employee("Renee", "contract", 3000, 0, 0, 4, 200)
jan = Employee("Jan", "contract", 0, 150, 25, 3, 220)
robbie = Employee("Robbie", "monthly", 2000, 0, 0, 0, 0, 1500)
ariel = Employee("Ariel", "contract", 0, 120, 30, 0, 600)

