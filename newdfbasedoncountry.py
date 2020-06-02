def newdfbasedoncountry(dataframe,country):
    return dataframe[dataframe['Country/Region']== country]