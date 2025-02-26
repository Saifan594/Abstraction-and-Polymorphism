print("\033c")
print("\033[3m")
print("\033[1m")

class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")
    
    def language(self):
        print("Bengali is the most widely spoken language of Bangladesh.")
    
    def type(self):
        print("Bangladesh is a developing country.")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    
    def language(self):
        print("English is the most widely spoken language of USA.")
    
    def type(self):
        print("USA is a developing country.")

objBan = Bangladesh()
objUSA = USA()

for country in (objBan, objUSA):
    country.capital()
    country.language()
    country.type()
    print()