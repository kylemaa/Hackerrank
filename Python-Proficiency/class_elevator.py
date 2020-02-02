class Elevator:
    """C1M5L2_Methods_and_Classes_V3 GOOGLE Python methods and classes example"""

    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.top = 10
        self.bottom = -1
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


elevator = Elevator(-1, 10, 0)
