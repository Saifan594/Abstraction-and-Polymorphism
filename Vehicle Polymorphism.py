print("\033c")

class BMW:
    def fuelType(self):
        print("The fuel type of BMW is diesel.")
    
    def maxSpeed(self):
        print("The max speed of BMW is 305 km/h.")
    
    def price(self):
        print("The price of BMW is $149K.")

class Ferrari:
    def fuelType(self):
        print("The fuel type of Ferrari is petrol.")
    
    def maxSpeed(self):
        print("The max speed of Ferrari is 349 km/h.")
    
    def price(self):
        print("The price of Ferrari is $4M.")

class Tesla:
    def fuelType(self):
        print("The fuel type of Tesla is electricity.")
    
    def maxSpeed(self):
        print("The max speed of Tesla is 322 km/h.")
    
    def price(self):
        print("The price of Tesla is $119K.")

bmw = BMW()
ferrari = Ferrari()
tesla = Tesla()

for vehicle in (bmw, ferrari, tesla):
    vehicle.fuelType()
    vehicle.maxSpeed()
    vehicle.price()
    
    print()