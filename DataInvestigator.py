
import pandas as pd

class DataInvestigator:

    def __init__(self, df: pd.DataFrame):

        if isinstance(df, pd.DataFrame) and not df.empty:
            self.df = df

        else:
            self.df = None

    def baseline(self, col):
        if self.df is None:
            return None


    def corr(self, col1, col2):
        if self.df is None:
            return None


    def zeroR(self, col):
        return self.baseline(col)