
import pandas as pd

class DataInvestigator:

    def __init__(self, df: pd.DataFrame):

        if not isinstance(df, pd.DataFrame):
            self.df = None
            return
        if df.empty:
            self.df = None
            return

        self.df = df

    def baseline(self, col):
        pass

    def corr(self, col1, col2):
        pass

    def zeroR(self, col):
        pass