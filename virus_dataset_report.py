import os
import pandas as pd
import matplotlib.pyplot as plt


FILENAME = "test files/covid_19_clean_complete.csv"

def createdataframe(filename):
    """
    creates a dataframe.
    Args:
        filename: a csv file
    Returns:
        a dataframe
    """
    return pd.read_csv(filename)




def main():
    """ main function """
    info = []
    df = createdataframe(FILENAME)
    print(df.head())
    os.system("pause")

if __name__ == '__main__':
    main()