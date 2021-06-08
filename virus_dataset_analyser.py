"""
Virus dataset analyser
"""
from tkinter import Tk, Menu, filedialog, simpledialog
from tkinter import messagebox as msg
from tkinter.constants import Y
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def helpmenu():
    """ help menu funciton """
    msg.showinfo("Help", "You can find valuable information from Kaggle's datasets about viruses")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Version 1.0")
class VirusDatasetAnalyser():
    """VirusDatasetAnalysers class"""
    def __init__(self, master):
        self.master = master
        self.master.title("Virus_Dataset_Analyser")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.filename = ""
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv",
                                   accelerator='Ctrl+O', command=self.insert_csv)
        self.file_menu.add_command(label="Close file",
                                   accelerator='Ctrl+F4', command=self.closefile)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show infected countries",
                                   accelerator='Ctrl+S', command=self.infcountries)
        self.show_menu.add_command(label="Show most infected",
                                   accelerator='Alt+M', command=self.maxcases)
        self.show_menu.add_command(label="Show least infected",
                                   accelerator='Ctrl+M', command=self.mincases)
        self.show_menu.add_command(label="Show infected difference",
                                   accelerator='Alt+S', command=self.showinfdiff)
        self.show_menu.add_command(label="Show number of active cases by country",
                                   accelerator='Alt+T', command=self.active_cases)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.save_menu = Menu(self.menu, tearoff=0)
        self.save_menu.add_command(label="Deaths", command=lambda: self.splot("deaths"))
        self.save_menu.add_command(label="Confirmed", command=lambda:self.splot("confirmed"))
        self.save_menu.add_command(label="Recovered", command=lambda:self.splot("recovered"))
        self.save_menu.add_command(label="All", command=lambda: self.splot("all"))
        self.menu.add_cascade(label="Save Plots", menu=self.save_menu)
        self.cases_graph_menu = Menu(self.menu, tearoff=0)
        self.cases_graph_menu.add_command(label="Show cases by country",
                                          accelerator='Ctrl+T', command=self.casesbycountry)
        self.cases_graph_menu.add_command(label="Time series", accelerator='Ctrl+P',
                                          command=lambda: self.time_series_of('all'))
        self.cases_graph_menu.add_command(label="Time series of deaths", accelerator='Ctrl+D',
                                          command=lambda: self.time_series_of('Deaths'))
        self.cases_graph_menu.add_command(label="Time series of confirmed", accelerator='Alt+D',
                                          command=lambda: self.time_series_of('Confirmed'))
        self.cases_graph_menu.add_command(label="Time series of recovered", accelerator='Ctrl+R',
                                          command=lambda: self.time_series_of('Recovered'))
        self.menu.add_cascade(label="Graphs", menu=self.cases_graph_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-d>', lambda event: self.time_series_of('Deaths'))
        self.master.bind('<Alt-d>', lambda event: self.time_series_of('Confirmed'))
        self.master.bind('<Control-r>', lambda event: self.time_series_of('Recovered'))
        self.master.bind('<Alt-t>', lambda event: self.active_cases())
        self.master.bind('<Control-p>', lambda event: self.time_series_of('all'))
        self.master.bind('<Alt-m>', lambda event: self.maxcases())
        self.master.bind('<Control-m>', lambda event: self.mincases())
        self.master.bind('<Control-t>', lambda event: self.casesbycountry())
        self.master.bind('<Control-o>', lambda event: self.insert_csv())
        self.master.bind('<Control-F4>', lambda event: self.closefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-s>', lambda event: self.infcountries())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Alt-s>', lambda event: self.showinfdiff())

    def saveplots(df, state, indexlist):
        if state == 'all':
            y = ['Deaths', 'Confirmed', 'Recovered']
        elif state == "deaths":
            y = ['Deaths']
        elif state == "recovered":
            y = ['Recovered']
        else:
            y = ['Confirmed']
        for i in indexlist:
            df[df['Country/Region'] == str(i)].plot(figsize=(15, 10), x='Date', y=y, title=str(i))
            plt.savefig("plot/all/"+str(i)+".png")


    def active_cases(self):
        """ shows the number of active cases of a country """
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            self.user_input()
            msg.showinfo("Acitve Cases", "Active cases of "+
                         self.asked_country+
                         str(self.df[self.df['Country/Region'] == self.asked_country]
                             ['Confirmed'].sum()
                             -self.df[self.df['Country/Region'] == self.asked_country]
                             ['Deaths'].sum()
                             -self.df[self.df['Country/Region'] == self.asked_country]
                             ['Recovered'].sum()))
    def time_series_of(self, state):
        """ plots growth of Confirmed/Deaths/Recovered by time of a specific country"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            df = pd.read_csv(self.filename)
            self.user_input()
            if state == 'all':
                df[df['Country/Region'] == self.asked_country].plot(x='Date',
                                                                    y=['Confirmed',
                                                                       'Deaths',
                                                                       'Recovered'])
            else:
                df[df['Country/Region'] == self.asked_country].plot(x='Date', y=[state])
                plt.title("Time seris of "+ state+" for "+self.asked_country)
            plt.show()
    def showinfdiff(self):
        """ shows the differences an infected country based on two specific dates """
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
    def mincases(self):
        """ shows name the least confirmed/Deaths/Recoverd countries"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            msg.showinfo("Min",
                         "Least confirmed cases:"+
                         str(self.df[self.df.Confirmed == self.df.Confirmed.min()]
                             ['Country/Region'].to_string())+
                         "\nLeast Deaths cases:" +
                         str(self.df[self.df.Deaths == self.df.Deaths.min()]
                             ['Country/Region'].to_string())+
                         "\nLeast Recovered cases:"+
                         str(self.df[self.df.Recovered == self.df.Recovered.min()]
                             ['Country/Region'].to_string()))
    def maxcases(self):
        """ shows name the most confirmed/Deaths/Recoverd countries"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            msg.showinfo("Max",
                         "Most confirmed cases:"+
                         str(self.df[self.df.Confirmed == self.df.Confirmed.max()]['Country/Region'].to_string())+
                         "\nMost Deaths cases:"+
                         str(self.df[self.df.Deaths == self.df.Deaths.max()]['Country/Region'].to_string())+
                         "\nMost Recovered cases:"+
                         str(self.df[self.df.Recovered == self.df.Recovered.max()]['Country/Region'].to_string()))
    def closefile(self):
        """ closes the csv file """
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            self.filename = ""
            msg.showinfo("SUCCESS", "CSV FILE SUCCESSFULLY CLOSED")
    def infcountries(self):
        """ shows the number and the names of the infected countries """
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            msg.showinfo("Infected countries", "There are " +
                         str(len(self.df['Country/Region'])) +
                         " infected coutries. \n"+str(list(self.df['Country/Region'])))
    def user_input(self):
        """ user input for casesbycountry and time_series functions"""
        self.asked_country = simpledialog.askstring("Country", "Enter the name of the country")
        while  not self.df['Country/Region'].str.contains(str(self.asked_country)).any():
            self.asked_country = simpledialog.askstring("Country", "Enter the name of the country")
    def casesbycountry(self):
        """ plots an Deaths/Confirmed/Recovered cases graph of a chosen country"""
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            self.user_input()
            data = [self.df[self.df['Country/Region'] == str(self.asked_country)]['Deaths'].sum(),
                    self.df[self.df['Country/Region'] == str(self.asked_country)]['Confirmed'].sum(),
                    self.df[self.df['Country/Region'] == str(self.asked_country)]['Recovered'].sum()]
            plt.bar(np.arange(3), data)
            plt.xticks(np.arange(3), ('Deaths', 'Confirmed', 'Recovered'))
            plt.title(self.asked_country+" Deaths/Confirmed/Recovered Bar Chart")
            plt.show()
    def check_columns(self):
        """ checks the columns name from the importrd .csv file """
        if all([item in self.df.columns for item in ['Province/State',
                                                     'Country/Region',
                                                     'Lat', 'Long',
                                                     'Date', 'Confirmed',
                                                     'Deaths', 'Recovered']]):
            self.df.drop_duplicates(subset='Country/Region', keep='last', inplace=True)
            self.df['Country/Region'] = self.df['Country/Region'].astype("string")
            msg.showinfo("SUCCESS", "CSV FILE ADDED SUCCESSFULLY")
        else:
            self.filename = ""
            msg.showerror("ERROR", "NO PROPER CSV ")
    
    def splot(self, state):
        if self.filename == "":
            msg.showerror("ERROR", "NO FILE IMPORTED")
        else:
            df = pd.read_csv(self.filename)
            indexlist = df["Country/Region"].unique().tolist()
            self.saveplots(df, state, indexlist)
        
    def file_input_validation(self):
        """ user input validation """
        if ".csv" in self.filename:
            self.df = pd.read_csv(self.filename)
            self.check_columns()
        else:
            self.filename = ""
            msg.showerror("ERROR", "NO CSV IMPORTED")

    def insert_csv(self):
        """ insert csv function """
        if self.filename == "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
            self.file_input_validation()
        else:
            msg.showerror("Error", " A CSV FILE IS ALREADY OPEN")
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    VirusDatasetAnalyser(root)
    root.mainloop()
if __name__ == '__main__':
    main()
