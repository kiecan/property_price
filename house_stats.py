# Sale Types
NEW = "New Dwelling house /Apartment"
RESALE = "Second-Hand Dwelling house /Apartment"


class HouseStats:
    
    def __init__(self, data):
        self.property_types = data["Description of Property"].tolist()
        self.new_dwellings = self.property_types.count(NEW)
        self.secondhand_dwellings = self.property_types.count(RESALE)

        self.prices = data["Price (€)"].tolist()

    def get_new(self):
        new_houses_pct = self.new_dwellings / len(self.property_types) * 100
        print(f"New Houses: {round(new_houses_pct, 2)}%")

    def get_resales(self):
        resale_pct = self.secondhand_dwellings / len(self.property_types) * 100
        print(f"Resale: {round(resale_pct, 2)}%")

    def get_prices(self):
        print(self.prices)
