class Glassware:
    def __init__(self, material: str = "Borosilicate Glass"):
        self.material = material

    def clean(self) -> str:
        return f"Cleaning the {self.material} ware."


class Beaker(Glassware):
    def __init__(self, capacity_ml: int, material: str = "Borosilicate Glass"):
        super().__init__(material)
        self.capacity_ml = capacity_ml


class Tray:
    def __init__(self, beaker_capacity_ml: int = 250):
        self.beakers = [Beaker(capacity_ml=beaker_capacity_ml) for _ in range(5)]

    def __del__(self):
        print("Tray is being deleted. All contained Beakers are lost to the system.")

    def show_inventory(self):
        print(f"Tray contains {len(self.beakers)} items.")


lab_tray = Tray(beaker_capacity_ml=500)
lab_tray.show_inventory()

lab_tray = None
