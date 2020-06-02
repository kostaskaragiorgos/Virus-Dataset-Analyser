def plot_specific(dataframe,country,state):
    dataframe[dataframe['Country/Region']==country].plot(x='Date', y=[state])