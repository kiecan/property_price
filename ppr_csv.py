import requests
from pathlib import Path
import csv


CSV_ENCODING = "windows-1252"
DOWNLOAD_URL = "https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR"


class PropertyPriceRegisterCsv:

    def __init__(self, c: str, y: str, m: str):
        self.download_folder = "data"
        Path(self.download_folder).mkdir(parents=True, exist_ok=True)
        requests.packages.urllib3.disable_warnings()
        self.download_file = None
        self.normalized_file = None
        self.year = y
        self.month = m
        self.county = c
        self.get_data()
        self.normalize_csv()

    def get_data(self):
        url = f"https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-{self.year}-{self.month}-{self.county}.csv/$FILE/PPR-{self.year}-{self.month}-{self.county}.csv"
        print(url)
        r = requests.get(url, allow_redirects=True, verify=False)
        self.download_file = f"{self.download_folder}/{self.year}_{self.month}_{self.county}.csv"
        open(self.download_file, 'wb').write(r.content)

    def normalize_csv(self):
        self.normalized_file =  f"{self.download_folder}/{self.year}_{self.month}_{self.county}_parsed.csv"
        input_file = open(file=self.download_file, mode='r', encoding=CSV_ENCODING)
        output_file = open(self.normalized_file, 'w')
        data = csv.reader(input_file)
        writer = csv.writer(output_file)
        currency_symbol = '€'

        for line in data:
            line = [value.replace(currency_symbol, '') for value in line]
            writer.writerow(line)
