class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None
    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj
        
class Lab:
    def __init__(self, room_num):
        self.room_num = room_num

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")

mr_cruz.assigned_lab = chem_lab

print(f"{mr_cruz.name} the Technician is assigned to Room {mr_cruz.assigned_lab.
