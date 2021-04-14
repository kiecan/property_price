import requests
from ppr_csv import PprCsv

COUNTY = "Galway"
YEAR = "2020"
MONTH = "03"


def main():

    ppr_csv = PprCsv(COUNTY, YEAR, MONTH)


if __name__ == "__main__":
    exit(main())
