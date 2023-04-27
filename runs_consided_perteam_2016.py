import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

matches_id_of_2016 = set()

extras_per_team = {}

#function that gives ID's of Matches Played in 2016 
def calculate_matches_2016 ():
    """ Calculating the ID of macthes in 2016"""
    with open('data/matches.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:

            if eachrow['season'] == '2016':
                matches_id_of_2016.add(eachrow['id'])


#Function that fills extras per team in 2016 dictionary
def extras_of_eachteam(eachrow ):
    """Calculationg Extras of each team"""
    if eachrow['match_id'] in matches_id_of_2016:
        if eachrow['bowling_team'] in extras_per_team:
            extras_per_team[eachrow['bowling_team']] += int(eachrow['extra_runs'])
        else :
            extras_per_team[eachrow['bowling_team']] = int(eachrow['extra_runs'])

def calculate ():
    """ CAlling calculate_matches_2016() and filling the extras_of_eachteam"""
    calculate_matches_2016()

    with open('data/deliveries.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            extras_of_eachteam(eachrow)


def plot ():
    """Ploting """
    team = list(extras_per_team.keys())

    extras = list(extras_per_team.values())

    plt.barh(team , extras)
    plt.title('Extras Of Each Team in 2016')
    plt.xlabel('Teams')
    plt.ylabel('Extras')
    plt.tight_layout()
    plt.show()


def exicute():
    """Exciuting the program"""
    calculate()
    plot()

exicute()

