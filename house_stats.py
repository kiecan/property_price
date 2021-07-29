# Sale Types
NEW = "New Dwelling house /Apartment"
RESALE = "Second-Hand Dwelling house /Apartment"


class HouseStats:
    
    def __init__(self, data, c: str) -> None:
        self.county = c
        self.number_of_sales = len(data.index)
        self.property_types = data["Description of Property"].tolist()
        self.new_dwellings = self.property_types.count(NEW)
        self.secondhand_dwellings = self.property_types.count(RESALE)
        self.prices = data["Price ()"].tolist()

    def get_new(self):
        new_houses_pct = self.new_dwellings / len(self.property_types) * 100
        new_houses_pct = round(new_houses_pct, 2)
        return new_houses_pct

    def get_resales(self):
        resale_pct = self.secondhand_dwellings / len(self.property_types) * 100
        resale_pct = round(resale_pct, 2)
        return resale_pct

    def get_prices(self):
        self.print_results(self.prices)
        return self.prices

    def get_number_of_sales(self) -> int:
        return self.number_of_sales

    def get_average_price(self) -> float:
        price_list = self.prices
        for i in range(0, len(price_list)):
          price_list[i] = price_list[i].replace(",","")
          price_list[i] = float(price_list[i])


        average_price = sum(price_list) / len(price_list)
        average_price =  round(average_price, 2)

        return average_price