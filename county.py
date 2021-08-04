from dataclasses import dataclass
from os import name

@dataclass
class County:
  """Class to track county information"""

  name: str
  new_house_pct: float
  resale_pct: float
  number_of_sales: int
  average_price: float
  month: str
  year:str

  def get_data(self):
    """Returns a dict of the counties data"""
    county_data = {
      "name": self.name,
      "new_house_pct": self.new_house_pct,
      "resale_pct": self.resale_pct,
      "number_of_sales": self.number_of_sales,
      "average_price": self.average_price,
      "month": self.month,
      "year": self.year
    }
    return county_data
