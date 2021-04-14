import requests
from pathlib import Path

class PprCsv:

    def __init__(self, c: str, y: str, m: str):
        self.county = c
        self.year = y
        self.month = m
        self.download_folder = "data"
        self.url = f"https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-{self.year}-{self.month}-{self.county}.csv/$FILE/PPR-{self.year}-{self.month}-{self.county}.csv"

        Path(self.download_folder).mkdir(parents=True, exist_ok=True)

        r = requests.get(self.url, allow_redirects=True, verify=False)

        open(f"{self.download_folder}/{self.county}_{self.month}_{self.month}.csv", 'wb').write(r.content)
