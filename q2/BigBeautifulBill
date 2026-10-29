class Bill:
    amount = 0
    def __init__(self, amount):
        self.amount = amount

    def pay(self, payment):
        self.amount -= payment.amount
        print("Paying with", payment.mode)
        print("Balance:", self.amount)
    #payment function goes here

class Payment:
    amount = 0
    mode = "Cash"
    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    def __init__(self,name,amount):
        self.mode = name
        self.amount = amount

bigBeautifulBill = Bill(1000)
bayad = Payment(900)
bigBeautifulBill.pay(bayad)

gcash = Ewallet("GCash",67)
bigBeautifulBill.pay(gcash)

ewallet = Ewallet("PisayCash", 33)
bigBeautifulBill.pay(ewallet)
