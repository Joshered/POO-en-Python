class Cake:
    def __init__(self, flavor):
        self.flavor=flavor

    def cut_in_part(self):
        print("Le gateau est coupé en 4 patie!")

cake = Cake("chocolate")
print(cake.flavor)
cake.cut_in_part()