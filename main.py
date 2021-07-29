from ppr_csv import PropertyPriceRegisterCsv
import pandas as pd
from house_stats import HouseStats
from county import County

COUNTIES = ["Carlow", "Dublin", "Wexford", "Wicklow", "Louth", "Kildare", "Meath", "Westmeath", "Kilkenny", 
"Laois", "Offaly", "Longford", "Clare", "Cork", "Kerry", "Limerick", "Tipperary", "Waterford", "Galway", 
"Leitrim", "Mayo", "Roscommon", "Sligo", "Cavan", "Donegal", "Monaghan"]

COUNTY = "DUBLIN"
YEAR = "2010"
MONTH = "04"

def main():

    COUNTIES.sort()

    county_list = []

    for c in COUNTIES:  
      ppr_csv = PropertyPriceRegisterCsv(c, YEAR, MONTH)
      house_data_set = pd.read_csv(ppr_csv.normalized_file)
      stats = HouseStats(house_data_set, c)

      county = County(c,stats.get_new(),stats.get_resales(),stats.get_number_of_sales(),stats.get_average_price())

      county_list.append(county)

    for county in county_list:
      print(f"###### {county.name} ######")
      print(f"Number of New Houses: {county.new_house_pct}%")
      print(f"Number of Resales: {county.resale_pct}%")
      print(f"Number of Sales: {county.number_of_sales}")
      print(f"Average Price: {county.average_price}")

if __name__ == "__main__":
    exit(main())
