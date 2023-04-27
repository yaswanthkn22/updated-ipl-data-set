import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


matches_won_by_each_team_season = {}

# This function produces a dictionary matches_won_by_each_team_season as keys are seasons and another dictinary as value which has team as key and matches won as value
def calculate_matches_won (eachrow ):
    """Filling matches_won_by_each_team_season
    """
    if eachrow['season'] in matches_won_by_each_team_season:
        if eachrow['team1'] in matches_won_by_each_team_season[eachrow['season']]:
            if int(eachrow['win_by_runs']) > 0 :
                matches_won_by_each_team_season[eachrow['season']][eachrow['team1']] += 1
        else :
            matches_won_by_each_team_season[eachrow['season']][eachrow['team1']] = 0

        if eachrow['team2'] in matches_won_by_each_team_season[eachrow['season']]:
            if int(eachrow['win_by_wickets']) > 0:
                matches_won_by_each_team_season[eachrow['season']][eachrow['team2']] += 1
        else :
            matches_won_by_each_team_season[eachrow['season']][eachrow['team2']] = 0
    
    else :
        matches_won_by_each_team_season[eachrow['season']] = dict()

        if int(eachrow['win_by_runs']) > 0:
            matches_won_by_each_team_season[eachrow['season']][eachrow['team1']] = 1
        else :
            matches_won_by_each_team_season[eachrow['season']][eachrow['team1']] = 0
        if int(eachrow['win_by_wickets']) > 0:
            matches_won_by_each_team_season[eachrow['season']][eachrow['team2']] = 1
        else :
            matches_won_by_each_team_season[eachrow['season']][eachrow['team2']] = 0



def calculate():
    """Callling calculate_matches_won() and reading CSV file"""
    with open ('data/matches.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            calculate_matches_won(eachrow)


def plot ():
    """PLots the data by unpacking the above dictionary"""
    seasons = list (matches_won_by_each_team_season.keys())
    seasons.sort()
    # Filling this dictionary with according to season and Team as value and List of matches orders by season as value
    each_team_wins = {}

    for season in seasons:
        index = seasons.index(season)
        for team , match_count in matches_won_by_each_team_season[season].items():
            
            if team in each_team_wins:  
                each_team_wins[team][index] += match_count
            else :
                each_team_wins[team] = [0]*len(seasons)
                each_team_wins[team][index] = match_count

    #Unpacking above each_team_wins to teams and matches_won
    teams = []
    matches_won = []
    for team , matches in each_team_wins.items():
        teams.append(team)
        matches_won.append(matches)       

    #ploting of Graph
    print(teams)
    print(matches_won)
    bars = []
    plt.title('Matches won by Each Team Each Year')
    bar = plt.bar(seasons , matches_won[0],label=teams[0])
    bars.append(bar)
    bottom = matches_won[0]
    print(bottom)
    for i in range(0 , len(teams)):

        bar = plt.bar(seasons, matches_won[i] , bottom = bottom)
        for j in range(0,len(seasons)):
            bottom[j] = matches_won[i][j] + bottom[j]
        bars.append(bar)
    
    plt.legend(bars , teams ,fontsize='6')
    plt.xlabel('seasons')
    plt.ylabel('Number of Matches Won')
    plt.tight_layout()
    plt.show()

def exicute():
    """Calls calculate() and plot()"""
    calculate()
    plot()

exicute()

       
    



        

            
            
