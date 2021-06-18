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

def cleardataframe(dataframe):
    """ removes the duplicate values
    Args:
        dataframe: a dataframe
    Returns:
        a modified dataframe
    """
    dataframe = dataframe.drop_duplicates(subset='location', keep='last')
    return dataframe

def addtoafile(data, flag):
    """
    write data to a .txt file
    Args:
        data: data to the file save
    """
    with open('dailyreport.txt', flag) as f:
        f.writelines(data)


def main():
    """ main function """
    info = []
    df = createdataframe(FILENAME)
    print(df.head())
    os.system("pause")

if __name__ == '__main__':
    main()