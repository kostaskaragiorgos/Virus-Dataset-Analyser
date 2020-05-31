def plot_cases(dataframe, country):
    dataframe[dataframe['Country/Region']==country].plot(x='Date', y=['Confirmed','Deaths','Recovered'])
