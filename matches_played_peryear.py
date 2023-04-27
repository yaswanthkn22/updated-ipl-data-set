import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

matches_per_year = {}

#function that calculates the number of matches
def matches (eachrow ):
    """ Filling matches_per_year"""
    if eachrow['season'] in matches_per_year:
        matches_per_year[eachrow['season']] += 1
    else :
        matches_per_year[eachrow['season']] = 1



def calculate ():
    """ Reading CSV file"""

    with open ('data/matches.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            matches(eachrow )


#plot function

def plot():
    """ Calculationg X and Y axis for ploting """
    season = list(matches_per_year.keys())
    matches_played = list(matches_per_year.values())

    plt.bar(season , matches_played)
    plt.title('Matches per Season')
    plt.xlabel('Season')
    plt.ylabel('Number Of Matches')
    plt.tight_layout()
    plt.show()

def exicute ():
    """ Exicute function calls calculate() and plot()"""
    calculate()
    plot()


exicute()
    

