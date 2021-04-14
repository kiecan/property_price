from ppr_csv import PprCsv
from parse_csv import ParseCsv
from house_stats import HouseStats

COUNTY = "Galway"
YEAR = "2010"
MONTH = "04"


def main():

    ppr_csv = PprCsv()
    ppr_csv.get_data(COUNTY, YEAR, MONTH)

    pc = ParseCsv(ppr_csv.output_file)

    data = pc.parse_file()

    hs = HouseStats(data)
    hs.get_new()
    hs.get_resales()


if __name__ == "__main__":
    exit(main())
