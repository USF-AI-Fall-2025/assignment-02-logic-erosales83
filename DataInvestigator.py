
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

        column = self.df.get(self.df.columns[col])

        if column is None or column.empty:
            return None

        values = column.mode()
        return values.iloc[0]


    def corr(self, col1, col2):
        if self.df is None:
            return None


    def zeroR(self, col):
        return self.baseline(col)