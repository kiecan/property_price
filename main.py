from ppr_downloader import PropertyPriceRegisterDownloader
import pandas as pd
from house_stats import HouseStats
from county import County

def main():

    ppr_downloader = PropertyPriceRegisterDownloader()

    file_dict = ppr_downloader.generate_file_names()

    county_data = []

    for file, county_name in file_dict.items():
      downloaded_file = ppr_downloader.get_data(file)
      parsed_file = ppr_downloader.normalize_csv(downloaded_file)
      house_data_set = pd.read_csv(parsed_file)
      housing_stats = HouseStats(house_data_set, county_name)
      county_stats = County(county_name,housing_stats.get_new(),housing_stats.get_resales(),housing_stats.get_number_of_sales(),housing_stats.get_average_price(),housing_stats.month,housing_stats.year)
      county_data.append(county_stats)  

    row_list = []
    for row in county_data:
      row_list.append(row.get_data())
    total_df = pd.DataFrame(row_list)

    print(total_df)

if __name__ == "__main__":
    exit(main())
