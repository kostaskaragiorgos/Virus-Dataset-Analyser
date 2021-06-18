import logging
import os
import pandas as pd
import matplotlib.pyplot as plt


FILENAME = "test files/covid_19_clean_complete.csv"

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

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
    dataframe = dataframe.drop_duplicates(subset='Country', keep='last')
    return dataframe

def getcasesplotforeverylocation(dataframe):
    """
    Saves a Vaccinations plot for every location.
    Args:
        dataframe: a pandas dataframe
    """
    indexlist = dataframe.Country.unique().tolist()
    for i in indexlist:
        if str(i) == "Taiwan*":
            i = "Taiwan"
        dataframe[dataframe['Country'] == str(i)].plot(figsize=(15, 10), x='Date', y=['Confirmed', 'Deaths', 'Recovered'], title="Cases of "+str(i))
        plt.savefig("plots/Cases of "+str(i)+".png")

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
    logging.info("dataset file has been successfully imported")
    getcasesplotforeverylocation(df)
    logging.info("Cases plots have been successfully created")
    df = cleardataframe(df)
    os.system("pause")

if __name__ == '__main__':
    main()