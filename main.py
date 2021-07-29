from ppr_csv import PropertyPriceRegisterCsv
import pandas as pd
from house_stats import HouseStats
from county import County

COUNTIES = ["Carlow", "Dublin", "Wexford", "Wicklow", "Louth", "Kildare", "Meath", "Westmeath", "Kilkenny", 
"Laois", "Offaly", "Longford", "Clare", "Cork", "Kerry", "Limerick", "Tipperary", "Waterford", "Galway", 
"Leitrim", "Mayo", "Roscommon", "Sligo", "Cavan", "Donegal", "Monaghan"]
MONTHS = ["01","02","03","04","05","06","07","08","09","10","11","12"]
YEARS = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]

YEAR = "2021"
MONTH = "04"

def main():

    COUNTIES.sort()

    county_data = []
    county_names = []
    county_new = []
    county_resale = []
    county_sales = []
    county_average = []
    county_months = []
    county_years = []

    for c in COUNTIES:  
      for y in YEARS:
        for m in MONTHS:
          ppr_csv = PropertyPriceRegisterCsv(c, y, m)
          house_data_set = pd.read_csv(ppr_csv.normalized_file)
          stats = HouseStats(house_data_set, c)

          county = County(c,stats.get_new(),stats.get_resales(),stats.get_number_of_sales(),stats.get_average_price(),m,y)

          county_data.append(county)

    for county in county_data:
      county_names.append(county.name)
      county_new.append(county.new_house_pct)
      county_resale.append(county.resale_pct)
      county_sales.append(county.number_of_sales)
      county_average.append(county.average_price)
      county_months.append(county.month)
      county_years.append(county.year)

    all_data = {'county':county_names, 'new_pct':county_new, 'resale_pct':county_resale, 'sales':county_sales, 'average_price':county_average, 'month':county_months, 'year':county_years}

    county_df = pd.DataFrame(data=all_data)

    county_df.to_csv(index=False,path_or_buf="data.csv")

    #print(county_df)


if __name__ == "__main__":
    exit(main())
