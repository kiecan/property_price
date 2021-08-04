from typing import Dict, List
import requests
from pathlib import Path, PosixPath
#import logging
import csv
import datetime


CSV_ENCODING = "windows-1252"
DOWNLOAD_URL = "https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/"
COUNTIES = ["Carlow", "Dublin", "Wexford", "Wicklow", "Louth", "Kildare", "Meath", "Westmeath", "Kilkenny", 
"Laois", "Offaly", "Longford", "Clare", "Cork", "Kerry", "Limerick", "Tipperary", "Waterford", "Galway", 
"Leitrim", "Mayo", "Roscommon", "Sligo", "Cavan", "Donegal", "Monaghan"]

class PropertyPriceRegisterDownloader:

    def __init__(self):
        self.download_folder = "data"
        Path(self.download_folder).mkdir(parents=True, exist_ok=True)
        requests.packages.urllib3.disable_warnings()
        self.download_file : str
        self.normalized_file : str
        #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    def get_data(self, filename:str) -> PosixPath:
        """Downloads the given filename from Property Price Register if not exits. Returns name of file as PosixPath"""
        url = f"{DOWNLOAD_URL}/{filename}/$FILE/{filename}"

        file = Path(f"{self.download_folder}/{filename}")
        if not file.is_file():
          print(f"Downloading {file}...")
          r = requests.get(url, allow_redirects=True, verify=False)
          open(file, 'wb').write(r.content)
        #else:
        #  print(f"{file} exists")

        return file


    def normalize_csv(self, filename:PosixPath) -> None:
        """Removes the Euro Symbol from the file and saves as parsed file. Returns name of normalized file"""
        normalized_file = self.append_filename(filename, "_parsed")
        if not normalized_file.is_file():
          input_file = open(file=filename, mode='r', encoding=CSV_ENCODING)
          output_file = open(normalized_file, 'w')
          data = csv.reader(input_file)
          writer = csv.writer(output_file)
          currency_symbol = '€'

          for line in data:
              line = [value.replace(currency_symbol, '') for value in line]
              writer.writerow(line)
        #else:
        #  print(f"{normalized_file} already processed")
        return normalized_file


    def generate_month_numbers(self) -> List:
      """Returns a list from 01 to 12 to represent months"""
      return ["%.2d" % i for i in range(1,13)]

    def generate_years(self) -> List:
      """Returns a list of years from 2010 to now"""
      current_year = datetime.datetime.now()
      return list(range(2010, current_year.year+1))

    def generate_file_names(self) -> Dict:
      """Generates dict of filenames to download with their counties in format {'filename': 'county'}. Returns a dict"""
      current_datetime = datetime.datetime.now()

      COUNTIES.sort()
      file_dict = {}
      for c in COUNTIES:
        for m in self.generate_month_numbers():
          for y in self.generate_years():
            if int(y) >= current_datetime.year and int(m) >= current_datetime.month:
              break
            else:
              file_dict[str(f"PPR-{y}-{m}-{c}.csv")] = c
      return file_dict

    def append_filename(self, path: str, append_string: str) -> PosixPath:
      """Append string to a given CSV file. Returns new file path"""
      file_path = path

      path_parts = list(file_path.parts)
      path_parts[-1] = path_parts[-1].replace(".csv", f"{append_string}.csv")
      parsed_file_path = Path('/'.join(path_parts))

      return parsed_file_path