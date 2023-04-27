import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

season_team_matches_dist = {}


#this function creates a disctionary of seasons as keys and another dictionary of teams and matchhes at that season
def calculate_data (eachrow):
    """ Filling season_team_matches_dist Dictionary"""
    if eachrow['season'] in season_team_matches_dist:
        if eachrow['team1'] in season_team_matches_dist[eachrow['season']] :
            season_team_matches_dist[eachrow['season']][eachrow['team1']] += 1
        else :
            season_team_matches_dist[eachrow['season']][eachrow['team1']] = 1
        
        if eachrow['team2'] in season_team_matches_dist[eachrow['season']]:
            season_team_matches_dist[eachrow['season']][eachrow['team2']] += 1
        else :
            season_team_matches_dist[eachrow['season']][eachrow['team2']] = 1
    else :
        season_team_matches_dist[eachrow['season']] =dict()
        season_team_matches_dist[eachrow['season']][eachrow['team1']] = 1
        season_team_matches_dist[eachrow['season']][eachrow['team2']] = 1


def calculate():
    """ Reading CSV File"""

    with open('data/matches.csv',encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            calculate_data(eachrow)


def plot ():
    """ Plot Function calculates the data required """
    calculate()
    seasons = list(season_team_matches_dist.keys())
    seasons.sort()
    print(seasons)
    teams_and_matches = {}
    
    # Here we are creating a dictinary of teams as keys and matches played (value) as a list of size eqial to seasons

    for season in seasons:
        index = seasons.index(season)
        for team , match_count in season_team_matches_dist[season].items():
            if team in teams_and_matches:
                
                teams_and_matches[team][index]=match_count
            else :
                teams_and_matches[team]=[0] * len(seasons)
                teams_and_matches[team][index]=match_count
    
    print(teams_and_matches)
    
    #unpacking the above dictionary to teams and list of match counts
    
    teams = []
    match_count = []

    for team , count in teams_and_matches.items():
        teams.append(team)
        match_count.append(count)

    #plotting a stacked bar chart bottom shuld be updated
    plt.title('Number of Games Per season Per Team')
    plt.xlabel('Matches')
    plt.ylabel('Seasons')
    bars=[]
    bar = plt.bar(seasons,match_count[0],label = teams[0])
    bars.append(bar)
    bottom = match_count[0]
    for i in range(1,len(teams)):

        bar = plt.bar(seasons, match_count[i],bottom=bottom, label=teams[i])

        #here updating bottom by adding previous bottm vallues to current matchcount
        for j in range(0, len(seasons)):
            bottom[j]=match_count[i][j]+bottom[j]
        
        bars.append(bar)

    #To get legend
    plt.legend(bars,teams , fontsize= '7')
    plt.tight_layout()
    plt.show()

        
        

    
    print(seasons)
    

def exicute ():
    """ Excicute function to perfarm all the tasks"""
    plot()

exicute()