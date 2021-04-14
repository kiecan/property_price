from ppr_csv import PprCsv

COUNTY = "Galway"
YEAR = "2020"
MONTH = "03"


def main():

    ppr_csv = PprCsv()
    ppr_csv.get_data(COUNTY, YEAR, MONTH)


if __name__ == "__main__":
    exit(main())
