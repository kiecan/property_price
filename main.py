from ppr_downloader import PropertyPriceRegisterDownloader
import pandas as pd
from house_stats import HouseStats
from county import County

def main():

    county_data = []
    county_names = []
    county_new = []
    county_resale = []
    county_sales = []
    county_average = []
    county_months = []
    county_years = []


    ppr_downloader = PropertyPriceRegisterDownloader()

    file_dict = ppr_downloader.generate_file_names()

    for file, county_name in file_dict.items():
      downloaded_file = ppr_downloader.get_data(file)
      parsed_file = ppr_downloader.normalize_csv(downloaded_file)
    

      house_data_set = pd.read_csv(parsed_file)
      print(house_data_set)
      housing_stats = HouseStats(house_data_set, county_name)

      print(housing_stats.county,housing_stats.get_number_of_sales())


      #county_stats = County(county_name,stats.get_new(),stats.get_resales(),stats.get_number_of_sales(),stats.get_average_price(),m,y)

    #county_data.append(county)

    # for county in county_data:
    #   county_names.append(county.name)
    #   county_new.append(county.new_house_pct)
    #   county_resale.append(county.resale_pct)
    #   county_sales.append(county.number_of_sales)
    #   county_average.append(county.average_price)
    #   county_months.append(county.month)
    #   county_years.append(county.year)


    #all_data = {'county':county_names, 'new_pct':county_new, 'resale_pct':county_resale, 'sales':county_sales, 'average_price':county_average, 'month':county_months, 'year':county_years}

    #county_df = pd.DataFrame(data=all_data)

    #county_df.to_csv(index=False,path_or_buf="data.csv")

    #print(county_df)


if __name__ == "__main__":
    exit(main())
