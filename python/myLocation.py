class Location:
    def __init__(self,name,country):
        self.name = name
        self.country = country
    
    def myLocation(self):
        print("Hola, soy "+self.name+" y vivo en "+self.country)

loc = Location("Amaury","Colombia")
loc.myLocation()