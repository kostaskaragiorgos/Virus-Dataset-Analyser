def cases_difference(dataframe, country,f_date,to_date,state):
    number_of_deaths_f = dataframe.loc[(dataframe['Country/Region']==country) &(dataframe['Date']==f_date)][state]
    number_of_deaths_t = dataframe.loc[(dataframe['Country/Region']==country) &(dataframe['Date']==to_date)][state]
    return "Number of "+state+" from "+f_date+" to "+to_date+" in "+country+" "+str( abs(int(number_of_deaths_f)-int(number_of_deaths_t)))