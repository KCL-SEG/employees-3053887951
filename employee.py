"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.total_pay = 0

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        return f"{self.name} works."

class MonthlyEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.total_pay = monthly_salary

    def __str__(self):
        return f"{super().__str__()} Their total pay is {self.total_pay}."

class ContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.total_pay = hours_worked * hourly_rate

    def __str__(self):
        return f"{super().__str__()} Their total pay is {self.total_pay}."

class BonusCommissionEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.total_pay += bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.total_pay - getattr(self, 'monthly_salary', 0)}."

class HourlyBonusCommissionEmployee(ContractEmployee):
    def __init__(self, name, hours_worked, hourly_rate, bonus_commission):
        super().__init__(name, hours_worked, hourly_rate)
        self.total_pay += bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.total_pay - getattr(self, 'hours_worked', 0) * getattr(self, 'hourly_rate', 0)}."

class CommissionEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, commission_rate, num_contracts):
        super().__init__(name, monthly_salary)
        commission = commission_rate * num_contracts
        self.total_pay += commission

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {num_contracts} contract(s) at {commission_rate}/contract."

class HourlyCommissionEmployee(ContractEmployee):
    def __init__(self, name, hours_worked, hourly_rate, commission_rate, num_contracts):
        super().__init__(name, hours_worked, hourly_rate)
        commission = commission_rate * num_contracts
        self.total_pay += commission

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {num_contracts} contract(s) at {commission_rate}/contract."


# Test cases
billie = MonthlyEmployee("Billie", 4000)
charlie = ContractEmployee("Charlie", 100, 25)
renee = CommissionEmployee("Renee", 3000, 200, 4)
jan = HourlyCommissionEmployee("Jan", 150, 25, 220, 3)
robbie = BonusCommissionEmployee("Robbie", 2000, 1500)
ariel = HourlyBonusCommissionEmployee("Ariel", 120, 30, 600)
