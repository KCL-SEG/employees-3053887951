"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, hours_worked=None, hourly_rate=None, bonus=None, commission_rate=None, num_contracts=None):
        self.name = name
        if hours_worked is not None and hourly_rate is not None:
            self.pay = hours_worked * hourly_rate + (bonus if bonus else 0)
        elif commission_rate is not None and num_contracts is not None:
            self.pay = pay + commission_rate * num_contracts
        else:
            self.pay = pay

    def get_pay(self):
        return self.pay

    def __str__(self):
        if hasattr(self, 'hours_worked'):  # Contract employee
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}.\nTheir total pay is {self.pay}."
        elif hasattr(self, 'commission_rate'):  # Commission employee
            return f"{self.name} works on a monthly salary of {self.pay} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract.\nTheir total pay is {self.pay}."
        else:  # Monthly salary employee
            return f"{self.name} works on a monthly salary of {self.pay}.\nTheir total pay is {self.pay}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", None, hours_worked=100, hourly_rate=25, bonus=0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", 3000, commission_rate=200, num_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", None, hours_worked=150, hourly_rate=25, bonus=3 * 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", 2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", None, hours_worked=120, hourly_rate=30, bonus=600)
