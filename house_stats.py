# Sale Types
from pandas.core.frame import DataFrame


NEW = "New Dwelling house /Apartment"
RESALE = "Second-Hand Dwelling house /Apartment"


class HouseStats:
    
    def __init__(self, data: DataFrame, c: str):
        self.county = data["County"].tolist().q
        self.number_of_sales = len(data.index)
        self.property_types = data["Description of Property"].tolist()
        self.new_dwellings = self.property_types.count(NEW)
        self.secondhand_dwellings = self.property_types.count(RESALE)
        self.prices = data["Price"].tolist()
        self.month = data[

    def get_new(self) -> float:
        new_houses_pct = self.new_dwellings / len(self.property_types) * 100
        new_houses_pct = round(new_houses_pct, 2)
        return new_houses_pct

    def get_resales(self) -> float:
        resale_pct = self.secondhand_dwellings / len(self.property_types) * 100
        resale_pct = round(resale_pct, 2)
        return resale_pct

    def get_prices(self):
        return self.prices

    def get_number_of_sales(self) -> int:
        """Returns the number of sales"""
        return self.number_of_sales

    def get_average_price(self) -> float:
        """Formats the price column to floar and calculates the average price for the month. Returns the average as float"""
        price_list = self.prices
        for i in range(0, len(price_list)):
          price_list[i] = price_list[i].replace(",","")
          price_list[i] = float(price_list[i])

        average_price = sum(price_list) / len(price_list)
        average_price =  round(average_price, 2)

        return average_price