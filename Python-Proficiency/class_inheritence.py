class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.top = top
        self.bottom = bottom
        self.current = current

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current == self.top:
            return
        self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current == self.bottom:
            return
        self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor > self.top:
            floor = self.top
        elif floor < self.bottom:
            floor = self.bottom
        self.current = floor

    def __str__(self):
        return "Current floor: {}".format(self.current)


elevator = Elevator(-1, 10, 0)
print(elevator)


class Clothing:
    """E-commerce for clothing inventory with method to count the material of the type of clothing"""
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        self.material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    """This class inherits the init, add_item, stock_by_material methods and dictionaries with Clothing class"""
    material = "Cotton"


class pants(Clothing):
    """This class inherits the init, add_item, stock_by_material methods and dictionaries with Clothing class"""

    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
