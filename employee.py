class Employee:
    def __init__(self, name):
        self.name = name
        self.total_pay = 0

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.total_pay}."

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

class CommissionEmployee(ContractEmployee):
    def __init__(self, name, hours_worked, hourly_rate, commission_rate, num_contracts):
        super().__init__(name, hours_worked, hourly_rate)
        commission = commission_rate * num_contracts
        self.total_pay += commission

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {num_contracts} contract(s) at {commission_rate}/contract."


class BonusCommissionEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.total_pay += bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {bonus_commission}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee("Billie", 4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee("Charlie", 100, 25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = CommissionEmployee("Renee", 0, 0, 200, 4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = CommissionEmployee("Jan", 150, 25, 220, 3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = BonusCommissionEmployee("Robbie", 2000, 1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = BonusCommissionEmployee("Ariel", 120, 30, 600)
