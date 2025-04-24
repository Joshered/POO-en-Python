class Drink:
    """une boisson"""
    def __init__(self,price):
        self.price = price
        
    def drink(self):
        print("Je ne sais pas ce que c'est, mais je le bois")
        
class Coffee(Drink):
    prices={"simple":1,"serre":1,"allongé":1.5}
    
    def __init__(self, type):
        self.type=type
        super().__init__(price=self.prices.get(type,1))
        
    def drink(self):
        print(f"Un bon café de {self.type} qui coute {self.price}$ pour me reveiller !")
        
coffee = Coffee("allonge")
boire= Coffee.drink()