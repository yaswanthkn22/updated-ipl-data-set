import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


batters_of_rcb = {}



#funtion to create a dictionary of runs by each team

def runsofeachbatter (eachrow):
    """Runs of Each Batter"""
    if eachrow['batting_team'] == 'Royal Challengers Bangalore' and eachrow['batsman'] in batters_of_rcb:
        batters_of_rcb[eachrow['batsman']]+=int(eachrow['batsman_runs'])
    else :
        if eachrow['batting_team'] == 'Royal Challengers Bangalore' and not (eachrow['batsman'] in batters_of_rcb) :
            batters_of_rcb[eachrow['batsman']]=int(eachrow['batsman_runs'])


#Calculate function for reading data from csv file and calls runsofeachbatter() each iteration

def calculate():
    """Reading CSV file and calling runsofeachbatter()"""

    with open('data/deliveries.csv',encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            runsofeachbatter(eachrow )

#plot fuuntion to plot a graph 
def plot():
    """Plotting the graph"""

    batters = []
    scores = []

    for batter , count in batters_of_rcb.items():
        batters.append(batter)
        scores.append(count)

    scores,batters = zip(*sorted(zip(scores,batters ), reverse=True))

    top_ten_batters = batters[:10]
    top_scores = scores[:10]

    print(top_ten_batters , top_scores)

    plt.bar(top_ten_batters,top_scores)
    plt.title('Top 10 RCB Batters')
    plt.xlabel('Batsman')
    plt.ylabel('Scores')
    plt.tight_layout()
    plt.show()
    

def exicute():
    """Callling calculate() and plot()"""
    calculate()
    plot()

exicute()

