import requests
from pathlib import Path


class PprCsv:

    def __init__(self):
        self.download_folder = "data"
        Path(self.download_folder).mkdir(parents=True, exist_ok=True)
        requests.packages.urllib3.disable_warnings()
        #self.output_file

    def get_data(self, county: str, year: str, month: str):
        url = f"https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-{year}-{month}-{county}.csv/$FILE/PPR-{year}-{month}-{county}.csv"
        r = requests.get(url, allow_redirects=True, verify=False)
        self.output_file = f"{self.download_folder}/{year}_{month}_{county}.csv"
        open(self.output_file, 'wb').write(r.content)
