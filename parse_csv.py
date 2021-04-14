import pandas as pd


class ParseCsv:

    def __init__(self, f:str):
        self.filename = f

    def parse_file(self):
        data = pd.read_csv(self.filename)
        return data
