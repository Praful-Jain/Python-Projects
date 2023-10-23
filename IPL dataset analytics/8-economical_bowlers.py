import csv
import matplotlib.pyplot as plt

def read_file(csv_file):
    # Open the CSV file for reading.
    with open(csv_file) as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        match_reader = list(csv_reader)  
    return match_reader


def execute(match_reader):            
    # Dictionary to store number of bowls bowled by a bowler
    bowls={}
    # Dictionary to store number of runs took by opponent
    runs={}
    
    for row in match_reader :
        if int(row['match_id']) >= 518 and int(row['match_id']) <=576 :
            if(row['wide_runs'] == '0' and row['noball_runs'] == '0') :
                bowls[row['bowler']] = bowls.get(row['bowler'] , 0) + 1
            runs[row['bowler']]  = runs.get(row['bowler'] , 0) + int(row['total_runs'])     
                  
    overs={}
    for player in bowls :
        overs[player] = bowls[player]/6 
        
    # Dictionary to store economy of each bowler
    economy = {}
    for player in runs :
        economy[player] = round(runs[player]/overs[player] , 2)
    
    # Sorting in ascending order
    economy = dict(sorted( economy.items() ,key = lambda x : x[1]))
    
    # Identifying top 10 bowlers based on their economy
    top10_bowler={}
    count=0
    for bowler in economy :
        top10_bowler[bowler] = economy[bowler]
        count += 1
        if(count==10) :
            break

    for i in top10_bowler :
        print(i," : ",economy[i])
    return top10_bowler


def plot(top10_bowler):
    # Plotting the bar graph
    plt.bar(top10_bowler.keys(),top10_bowler.values())
    plt.xlabel('Bowler Name')
    plt.xticks(rotation=90)
    plt.ylabel('Economic points')
    plt.title('Top 10 economical bowlers in the year 2015')
    plt.show()
    

match_reader = read_file('IPL dataset analytics/deliveries.csv')
top10_bowler = execute(match_reader)
plot(top10_bowler)