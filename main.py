from ppr_csv import PropertyPriceRegisterCsv
import pandas as pd
from house_stats import HouseStats


COUNTY = "Galway"
YEAR = "2020"
MONTH = "04"

def main():

    ppr_csv = PropertyPriceRegisterCsv(COUNTY, YEAR, MONTH)

    print(ppr_csv.normalized_file)

    house_data_set = pd.read_csv(ppr_csv.normalized_file)

    stats = HouseStats(house_data_set)

    stats.get_new()

    stats.get_resales()

    stats.get_prices()

    #print(data)

if __name__ == "__main__":
    exit(main())
