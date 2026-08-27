#Car Game 
class Car:
    def __init__(self, brand, model, battery = 33):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self,distance):
        self.battery -= distance / 25
        print("You traveled", distance, "km")
        print("Your", self.brand,self.model, "has", self.battery, "wh left")
    def charge(self,wH):
        self.battery += wH
        print("You charged your car")
        print("Your", self.brand,self.model, "has", self.battery, "wh left")

brand = input("What is the brand of your car? ")
model = input("What is the model of your car? ")
myCar = Car(brand,model)
while myCar.battery > 0:
    action = input("What do you want to do? (go, charge)")
    if action == "go":
        distance = int(input("How far? "))
        myCar.go(distance)
    elif action == "charge":
        wH = int(input("How much to charge? "))
        myCar.charge(wH)
    else:
        print("Invalid action")
print("Your car ran out of battery.")
