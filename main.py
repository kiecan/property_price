from ppr_csv import PprCsv
from parse_csv import ParseCsv
import csv
from house_stats import HouseStats
import string

COUNTY = "Galway"
YEAR = "2010"
MONTH = "04"
CSV_ENCODING = "windows-1252"


def main():

    ppr_csv = PprCsv(COUNTY, YEAR, MONTH)
    #ppr_csv.get_data(COUNTY, YEAR, MONTH)

    #pc = ParseCsv(ppr_csv.output_file)

    #data = pc.parse_file()

    #print(type(data))

    #hs = HouseStats(data)
    #hs.get_new()
    #hs.get_resales()
    #hs.get_prices()


if __name__ == "__main__":
    exit(main())
