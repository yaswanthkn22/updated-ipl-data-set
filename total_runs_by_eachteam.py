import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')



runs_by_eachteam = {}



#funtion to create a dictionary of runs by each team

def scoredruns(eachrow):
    """ Filling runs_by_eachteam Dictionary"""
    if eachrow['batting_team'] in runs_by_eachteam:
        runs_by_eachteam[eachrow['batting_team']]+=int(eachrow['total_runs'])
    else :
        runs_by_eachteam[eachrow['batting_team']]=int(eachrow['total_runs'])


#Calculate function for reading data from csv file and calls scoresruns each iteration

def calculate():
    """REading csv file and calling scoresruns()"""
    with open('data/deliveries.csv',encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            scoredruns(eachrow)

#plot fuuntion to plot a graph 
def plot():
    """Ploting a barh graph"""
    teams = list(runs_by_eachteam.keys())
    scores = list(runs_by_eachteam.values())


    plt.barh(teams,scores)
    plt.title('Total runs of each team Through History of IPL')
    plt.xlabel('Runs')
    plt.ylabel('Teams')
    plt.tight_layout()
    plt.show()
    

def exicute():
    """exciute function to call calculate() and plot()"""
    calculate()
    plot()

exicute()

