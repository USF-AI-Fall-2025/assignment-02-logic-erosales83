
import pandas as pd

class DataInvestigator:

    #Returns instance, checks if not empty
    def __init__(self, df: pd.DataFrame):

        if isinstance(df, pd.DataFrame) and not df.empty:
            self.df = df

        else:
            self.df = None

    #Returns the most frequent value of a given column
    def baseline(self, col):

        if self.df is None:
            return None

        column = self.df.get(self.df.columns[col])

        if column is None or column.empty:
            return None

        values = column.mode()
        return values.iloc[0]

    #Retruns the correlation between two given columns
    def corr(self, col1, col2):
        if self.df is None:
            return None

        column1 = self.df.get(self.df.columns[col1])
        column2 = self.df.get(self.df.columns[col2])

        if column1 is None or column1.empty:
            return None
        if column2 is None or column2.empty:
            return None

        correlation = column1.corr(column2)
        return correlation

    #Returns the most frequent value of a given column
    def zeroR(self, col):
        return self.baseline(col)

#Loads dataset, creates instance, and prints most frequent value
if __name__ == '__main__':
    df = pd.read_csv('gallstone.csv')
    di = DataInvestigator(df)
    print(di.baseline(1))